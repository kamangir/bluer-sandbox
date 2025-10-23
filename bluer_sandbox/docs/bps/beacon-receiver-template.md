title:::

```bash
@bps beacon - \
    --x $(@random --float 1) \
    --y $(@random --float 1) \
    --z $(@random --float 1) \
    --sigma $(@random --float 1) \
    --timeout 10
```

```text
🌀  bluer_sandbox.bps.utils.beacon: every 2 s for 10 s.
🌀  connected to system bus as :1.133
🌀  registering advertisement: x: 97.63, y: 88.52, z: 63.67, sigma: 59.24
🌀  advertising as 'sparrow3-back' (manuf 0xFFFF: <x,y,sigma>) - ^C to stop.
🌀  advertising sparrow3-back ...
🌀  advertising sparrow3-back ...
🌀  advertising sparrow3-back ...
🌀  advertising sparrow3-back ...
🌀  advertising sparrow3-back ...
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
🌀  bluer_sandbox.bps.utils.receiver: LE Scan for 10 s (Ctrl+C to stop) ...
🌀  scanning started...
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -40
🌀  x: 97.63, y: 88.52, z: 63.67, sigma: 59.24
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -40
🌀  x: 97.63, y: 88.52, z: 63.67, sigma: 59.24
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -49
🌀  x: 97.63, y: 88.52, z: 63.67, sigma: 59.24
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -48
🌀  x: 97.63, y: 88.52, z: 63.67, sigma: 59.24
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -48
🌀  x: 97.63, y: 88.52, z: 63.67, sigma: 59.24
🌀  timeout (10 s) reached, stopping advertisement.
🌀  scan stopped.
```