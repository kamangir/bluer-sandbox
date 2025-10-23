# bps: beacon-receiver

> ℹ️ tx-power is not implemented in rpi. nominal value: 10-12 dBm. -1: indicates unknown.

```bash
@bps beacon - \
    --x $(@random --float 1) \
    --y $(@random --float 1) \
    --z $(@random --float 1) \
    --sigma $(@random --float 1) \
    --timeout 10
```

```text
starting bluetooth...
⚙️  sudo systemctl start bluetooth
⚙️  sudo bluetoothctl power on
Changing power on succeeded
⚙️  sudo bluetoothctl discoverable on
AdvertisementMonitor path registered
⚙️  sudo -E /home/pi/venv/bluer_ai/bin/python3 -m bluer_sandbox.bps.utils.beacon --x 27.061946406295068 --y 39.12480033661038 --z 70.45884193445569 --sigma 70.31657557675341 --timeout 10
🌀  bluer_sandbox.bps.utils.beacon: every 2 s for 10 s.
🌀  connected to system bus as :1.31
⚠️  🌀  unknown tx_power reply.message_type: MessageType.ERROR
🌀  adapter TxPower=-1.0 dBm
🌀  registering advertisement: x: 27.06, y: 39.12, z: 70.46, sigma: 70.32, tx_power: -1.0 dBm
🌀  advertising as 'sparrow2' (manuf 0xFFFF: <x,y,z,sigma,tx_power>) - ^C to stop.
🌀  advertising sparrow2 ...
🌀  advertising sparrow2 ...
🌀  advertising sparrow2 ...
🌀  advertising sparrow2 ...
🌀  unregistered advertisement.
🌀  timeout (10 s) reached, stopping advertisement.
```

on another pi,

```bash
@bps receiver - \
    --grep sparrow \
    --timeout 10
```

```text
starting bluetooth...
⚙️  sudo systemctl start bluetooth
⚙️  sudo bluetoothctl power on
Changing power on succeeded
⚙️  sudo bluetoothctl discoverable on
Changing discoverable on succeeded
🌀  bluer_sandbox.bps.utils.receiver: LE Scan for 10 s (Ctrl+C to stop) ...
🌀  scanning started...
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow2
🌀  device address: B8:27:EB:41:BD:97
🌀  rssi: -66
🌀  x: 27.06, y: 39.12, z: 70.46, sigma: 70.32, tx_power: -1.00
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow2
🌀  device address: B8:27:EB:41:BD:97
🌀  rssi: -50
🌀  x: 27.06, y: 39.12, z: 70.46, sigma: 70.32, tx_power: -1.00
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow2
🌀  device address: B8:27:EB:41:BD:97
🌀  rssi: -51
🌀  x: 27.06, y: 39.12, z: 70.46, sigma: 70.32, tx_power: -1.00
🌀  timeout (10 s) reached, stopping advertisement.
🌀  scan stopped.
```
