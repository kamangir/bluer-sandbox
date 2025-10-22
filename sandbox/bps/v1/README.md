only works on rpi.

## test

```bash
@git @sandbox
git pull
cd sandbox/bps/v1
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
@git @sandbox
cd sandbox/bps/v1
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