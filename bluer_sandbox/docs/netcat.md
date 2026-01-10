# netcat

one machine 1,

```bash
@netcat listen
```

```text
type in "@netcat connect ip=192.168.43.61" to connect.
⚙️ nc -l 15000
hi
how are you
is it done?
Yes! :)
^C
```

on machine 2,

```bash
@netcat connect ip=192.168.43.61
```

```text
hi
how are you
is it done?
^C
```
