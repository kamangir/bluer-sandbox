# bps: beacon-receiver

> ℹ️ only works on rpi.

```bash
@bps beacon
```

```text
🌀  [beacon] Connected to system bus as :1.34
🌀  [beacon] Advertising started as 'TEST-PI' (manuf 0xFFFF: <x,y,sigma>)
🌀           Press Ctrl+C to stop.
🌀  ... advertising ...
🌀  ... advertising ...
...
🌀  ... advertising ...
^C🌀  [beacon] Unregistered advertisement.
```

on another pi,

```bash
@bps receiver
```

```text
LE Scan ...
48:11:E8:6C:64:E4 (unknown)
66:00:D6:B0:13:1B (unknown)
45:CC:27:15:F9:9D (unknown)
47:98:7A:B4:03:C6 (unknown)
7D:77:BC:08:F2:5D (unknown)
B8:27:EB:57:B6:DA (unknown)
47:98:7A:B4:03:C6 (unknown)
F4:67:26:36:2B:65 (unknown)
45:CC:27:15:F9:9D (unknown)
66:00:D6:B0:13:1B (unknown)
7D:77:BC:08:F2:5D (unknown)
B8:27:EB:57:B6:DA TEST-PI
```
