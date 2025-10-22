from bluezero import adapter, advertisement
import struct, time

ble_adapter = adapter.Adapter()
adv = advertisement.Advertisement(1, ble_adapter.address)
adv.local_name = "TEST-PI"
adv.manufacturer_data = {0xFFFF: struct.pack("<fff", 1.0, 2.0, 3.0)}
adv.start()
print("Advertising… (Ctrl+C to stop)")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    adv.stop()
