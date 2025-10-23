title:::

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
🌀  bluer_sandbox.bps.utils.beacon: every 2 s for 10 s.
🌀  connected to system bus as :1.41
⚠️  🌀  unknown tx_power reply.message_type: MessageType.ERROR
🌀  adapter TxPower=-1.0 dBm
🌀  registering advertisement: x: 67.52, y: 68.49, z: 3.03, sigma: 58.06, tx_power: -1.0 dBm
🌀  advertising as 'sparrow3-back' (manuf 0xFFFF: <x,y,z,sigma,tx_power>) - ^C to stop.
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
🌀  rssi: -67
🌀  x: 67.52, y: 68.49, z: 3.03, sigma: 58.06, tx_power: -1.00
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -51
🌀  x: 67.52, y: 68.49, z: 3.03, sigma: 58.06, tx_power: -1.00
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -50
🌀  x: 67.52, y: 68.49, z: 3.03, sigma: 58.06, tx_power: -1.00
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -49
🌀  x: 67.52, y: 68.49, z: 3.03, sigma: 58.06, tx_power: -1.00
🌀  . .. ... .. . .. ... .. . .. .
🌀  device name: sparrow3-back
🌀  device address: B8:27:EB:57:B6:DA
🌀  rssi: -49
🌀  x: 67.52, y: 68.49, z: 3.03, sigma: 58.06, tx_power: -1.00
🌀  timeout (10 s) reached, stopping advertisement.
🌀  scan stopped.
```