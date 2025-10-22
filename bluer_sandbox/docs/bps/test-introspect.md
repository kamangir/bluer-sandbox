# bps: test-introspect

> ℹ️ only works on rpi.

```bash
@bps install
```

---

```bash
@bps test
```

```text
🌀  bluer_sandbox.bps.test: connected to system bus with unique name: :1.20
🌀  exported org.example.Hello at /org/example/Hello
🌀  run in another terminal: "@bps introspect unique_bus_name=:1.20"
```

in another terminal,

```bash
"@bps introspect unique_bus_name=:1.20
```

```text
"Pong"
```

validate in the first window,

```text
🌀  bluer_sandbox.bps.test.ping() called by busctl!
```
