title:::

```bash
@bps beacon
```

```text
🌀  bluer_sandbox.bps.utils.beacon: connected to system bus as :1.87
🌀  bluer_sandbox.bps.utils.beacon: advertising as 'sparrow2' (manuf 0xFFFF: <x,y,sigma>) - ^C to stop.
🌀  advertising sparrow2 ...
🌀  advertising sparrow2 ...
🌀  advertising sparrow2 ...
^C🌀  bluer_sandbox.bps.utils.beacon: unregistered advertisement.
```

on another pi,

```bash
@bps receiver - \
    --grep sparrow
```

```text
🌀  bluer_sandbox.bps.utils.receiver: LE Scan for 10.0s (Ctrl+C to stop) ...
🌀  scanning started...
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow2
🌀  device address: B8:27:EB:41:BD:97
🌀  AdvertisementData(local_name='sparrow2', manufacturer_data={65535: b'\x9a\x99\x99?33\x13@\xcd\xccL?'}, rssi=-63)
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow2
🌀  device address: B8:27:EB:41:BD:97
🌀  AdvertisementData(local_name='sparrow2', manufacturer_data={65535: b'\x9a\x99\x99?33\x13@\xcd\xccL?'}, rssi=-46)
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow2
🌀  device address: B8:27:EB:41:BD:97
🌀  AdvertisementData(local_name='sparrow2', manufacturer_data={65535: b'\x9a\x99\x99?33\x13@\xcd\xccL?'}, rssi=-67)
🌀  timeout reached after 10.0s.
🌀  scan stopped.
```