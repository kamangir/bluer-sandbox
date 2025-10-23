title:::

```bash
@bps beacon
```

```text
🌀  bluer_sandbox.bps.utils.beacon: connected to system bus as :1.28
🌀  bluer_sandbox.bps.utils.beacon: advertising as 'sparrow3-back' (manuf 0xFFFF: <x,y,sigma>) - ^C to stop.
🌀  advertising sparrow3-back ...
🌀  advertising sparrow3-back ...
🌀  advertising sparrow3-back ...
🌀  advertising sparrow3-back ...
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
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -65
🌀  x: 1.20, y: 2.30, sigma: 0.80
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -50
🌀  x: 1.20, y: 2.30, sigma: 0.80
🌀  timeout reached after 10.0s.
🌀  scan stopped.
```