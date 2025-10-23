# aliases: bps

```bash
@bps \
	beacon \
	[~start_bluetooth] \
	[--x <1.0>] \
	[--y <2.0>] \
	[--sigma <3.0>] \
	[--spacing <2.0>] \
	[--timeout <10.0 | -1>]
 . start beacon.
@bps \
	install
 . install bps.
@bps \
	introspect \
	[~start_bluetooth,unique_bus_name=<1:234>]
 . introspect <1:234>.
@bps \
	receiver \
	[~start_bluetooth] \
	[--grep <sparrow>] \
	[--timeout <10>]
 . start receiver.
@bps \
	receiver \
	[~python,~start_bluetooth]
 . start receiver.
@bps \
	start_bluetooth
 . start bluetooth.
@bps \
	test \
	[~start_bluetooth]
 . d-bus ping test.
```
