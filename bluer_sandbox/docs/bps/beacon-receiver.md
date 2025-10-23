# bps: beacon-receiver

```bash
@bps beacon - \
    --x 1.1 \
    --y 2.2 \
    --sigma 3.3
```

```text
🌀  bluer_sandbox.bps.utils.beacon: connected to system bus as :1.85
🌀  registering advertisement: x: 1.10, y: 2.20, sigma: 3.30
🌀  advertising as 'sparrow3-back' (manuf 0xFFFF: <x,y,sigma>) - ^C to stop.
🌀  advertising sparrow3-back ...
...
🌀  advertising sparrow3-back ...
^C🌀  unregistered advertisement.
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
🌀  rssi: -51
🌀  x: 1.10, y: 2.20, sigma: 3.30
🌀  . .. ... .. . .. ... .. . .. .
...
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -41
🌀  x: 1.10, y: 2.20, sigma: 3.30
^C🌀  Ctrl+C detected, stopping scan ...
🌀  scan stopped.
```
