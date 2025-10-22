#!/usr/bin/env python3
"""
Raw-HCI hybrid beacon
---------------------
Each node alternates between:
  • sending a manufacturer-specific BLE advertisement (company ID 0xFFFF)
  • scanning for others' advertisements via Bleak

Works even when BlueZ strips ManufacturerData.
Run with:  sudo python3 beacon_hybrid_raw.py
"""

import asyncio, struct, time, socket, os
from bleak import BleakScanner

# --- Advertising constants ---
HCI_COMMAND_PKT = 0x01
OGF_LE_CTL = 0x08
OCF_LE_SET_ADVERTISING_PARAMETERS = 0x0006
OCF_LE_SET_ADVERTISING_DATA = 0x0008
OCF_LE_SET_ADVERTISE_ENABLE = 0x000A

COMPANY_ID = 0xFFFF


def hci_send_cmd(sock, ogf, ocf, data=b""):
    opcode = (ogf << 10) | ocf
    plen = len(data)
    sock.send(struct.pack("<BHB", HCI_COMMAND_PKT, opcode, plen) + data)


def advertise_once(sock, node_name="PI", x=1.0, y=2.0, sigma=0.5, duration=2.0):
    """Broadcast a single BLE advertisement frame for a few seconds."""
    payload = struct.pack("<fff", x, y, sigma)
    mdata = (
        bytes([len(payload) + 3, 0xFF, COMPANY_ID & 0xFF, COMPANY_ID >> 8]) + payload
    )
    name_bytes = node_name.encode()
    name = bytes([len(name_bytes) + 1, 0x09]) + name_bytes
    adv_data = mdata + name
    if len(adv_data) > 31:
        adv_data = adv_data[:31]

    # LE Set Advertising Parameters (9 fields on Broadcom)
    hci_send_cmd(
        sock,
        OGF_LE_CTL,
        OCF_LE_SET_ADVERTISING_PARAMETERS,
        struct.pack(
            "<HHBBB6sBHHB",
            0x00A0,  # min interval (100 ms)
            0x00A0,  # max interval
            0x00,  # adv type (ADV_IND)
            0x00,  # own addr type
            0x00,  # direct addr type
            b"\x00" * 6,  # direct addr
            0x07,  # channel map (37,38,39)
            0x00,  # filter policy
            0x00,  # unused (for alignment)
            0x00,  # unused
        ),
    )

    # Set Advertising Data
    hci_send_cmd(
        sock,
        OGF_LE_CTL,
        OCF_LE_SET_ADVERTISING_DATA,
        bytes([len(adv_data)]) + adv_data + bytes(31 - len(adv_data)),
    )

    # Enable advertising
    hci_send_cmd(sock, OGF_LE_CTL, OCF_LE_SET_ADVERTISE_ENABLE, b"\x01")
    time.sleep(duration)
    hci_send_cmd(sock, OGF_LE_CTL, OCF_LE_SET_ADVERTISE_ENABLE, b"\x00")


async def scan_once_bleak(t_scan=5.0):
    """Scan for other 0xFFFF manufacturer advertisements."""
    print(f"[hybrid] bleak scanning for {t_scan:.1f}s …")
    devices = await BleakScanner.discover(timeout=t_scan, return_adv=True)
    peers = {}
    for d, adv in (
        devices.items()
        if isinstance(devices, dict)
        else [(d, getattr(d, "advertisement_data", None)) for d in devices]
    ):
        if not adv:
            continue
        md = getattr(adv, "manufacturer_data", {})
        if COMPANY_ID in md and len(md[COMPANY_ID]) >= 12:
            x, y, sigma = struct.unpack("<fff", md[COMPANY_ID][:12])
            peers[d.address] = (x, y, sigma, d.rssi)
            print(
                f"[peer] {d.address:>17} RSSI={d.rssi:>4} "
                f"pos=({x:.1f},{y:.1f}) σ={sigma:.2f}"
            )
    if not peers:
        print("[hybrid] no peers detected")
    return peers


async def main():
    node = os.uname().nodename
    x, y, s = 1.0, 2.0, 0.5
    t_adv, t_scan = 2.0, 8.0

    sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_RAW, socket.BTPROTO_HCI)
    sock.bind((0,))

    print(f"[hybrid] node {node} ready (advertise {t_adv}s / scan {t_scan}s)")
    while True:
        advertise_once(sock, node_name=node, x=x, y=y, sigma=s, duration=t_adv)
        await asyncio.sleep(0.5)
        await scan_once_bleak(t_scan)
        await asyncio.sleep(0.5)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[hybrid] stopped")
