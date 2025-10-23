# bps: beacon-receiver

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
🌀  connected to system bus as :1.101
🌀  registering advertisement: x: 99.55, y: 14.48, sigma: 6.98
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
🌀  rssi: -60
🌀  x: 99.55, y: 14.48, sigma: 6.98
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -43
🌀  x: 99.55, y: 14.48, sigma: 6.98
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -44
🌀  x: 99.55, y: 14.48, sigma: 6.98
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -42
🌀  x: 99.55, y: 14.48, sigma: 6.98
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -43
🌀  x: 99.55, y: 14.48, sigma: 6.98
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -44
🌀  x: 99.55, y: 14.48, sigma: 6.98
🌀  timeout (10 s) reached, stopping advertisement.
🌀  scan stopped.
```
