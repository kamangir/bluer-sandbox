from bluezero import adapter, advertisement
import struct, time

ble_adapter = adapter.Adapter()
adv = advertisement.Advertisement(1, ble_adapter.address)
adv.local_name = "TEST-PI"
adv.manufacturer_data = {0xFFFF: struct.pack("<fff", 1.0, 2.0, 3.0)}
adv.start()

print("advertisement loop started ...")
try:
    while True:
        time.sleep(1)
        print("advertising ... (Ctrl+C to stop)")
except KeyboardInterrupt:
    adv.stop()
