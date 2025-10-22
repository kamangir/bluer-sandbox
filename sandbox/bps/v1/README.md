only works on rpi.

```bash
@git @sandbox
git pull
cd sandbox/bps/v1
```

## test & introspect

```bash
source bps.sh install,test
```

```text
starting test ...
⚙️  sudo -E /home/pi/venv/bluer_ai/bin/python3 test.py
[Python] Connected to system bus with unique name: :1.84
exported org.example.Hello at /org/example/Hello
run in another terminal: "source bps.sh introspect,N=:1.84"
```

in another terminal,

```bash
source bps.sh introspect,N=<N> # as printed by ^ command
```

```text
starting introspect ...
⚙️  sudo busctl --system introspect :1.84 /org/example/Hello --no-pager
NAME                                TYPE      SIGNATURE  RESULT/VALUE  FLAGS
org.example.Hello                   interface -          -             -
.Ping                               method    -          s             -
org.freedesktop.DBus.Introspectable interface -          -             -
.Introspect                         method    -          s             -
org.freedesktop.DBus.ObjectManager  interface -          -             -
.GetManagedObjects                  method    -          a{oa{sa{sv}}} -
.InterfacesAdded                    signal    oa{sa{sv}} -             -
.InterfacesRemoved                  signal    oas        -             -
org.freedesktop.DBus.Peer           interface -          -             -
.GetMachineId                       method    -          s             -
.Ping                               method    -          -             -
org.freedesktop.DBus.Properties     interface -          -             -
.Get                                method    ss         v             -
.GetAll                             method    s          a{sv}         -
.Set                                method    ssv        -             -
.PropertiesChanged                  signal    sa{sv}as   -             -
⚙️  sudo busctl --system call :1.84 /org/example/Hello org.example.Hello Ping
s "Pong"
```

then, in the first window,

```text
[Python] Ping() called by busctl
[Python] Ping() called by busctl
```

## beacon & receiver

```bash
source bps.sh beacon
```

```text
starting beacon ...
⚙️  sudo -E /home/pi/venv/bluer_ai/bin/python3 beacon.py
[Beacon] Connected to system bus as :1.126
[Beacon] Advertising started as 'TEST-PI' (manuf 0xFFFF: <x,y,sigma>)
         Press Ctrl+C to stop.
…advertising…
```

on another pi,

```bash
source bps.sh receiver
```

```text
starting receiver ...
LE Scan ...
5C:D0:82:22:02:1E (unknown)
63:B6:02:5F:1C:6E (unknown)
78:55:8C:68:23:99 (unknown)
7C:B4:E2:9A:EB:E2 (unknown)
77:35:A3:E1:F0:F4 (unknown)
C8:46:5E:98:9E:64 (unknown)
7C:B4:E2:9A:EB:E2 (unknown)
63:B6:02:5F:1C:6E (unknown)
5C:D0:82:22:02:1E (unknown)
77:35:A3:E1:F0:F4 (unknown)
B8:27:EB:57:B6:DA (unknown)
B8:27:EB:57:B6:DA TEST-PI
```