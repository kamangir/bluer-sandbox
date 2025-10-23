# aliases: bps

```bash
@bps \
	beacon \
	[~start_bluetooth,verbose] \
	[--x <1.0>] \
	[--y <2.0>] \
	[--z <3.0>] \
	[--sigma <4.0>] \
	[--spacing <2.0>] \
	[--timeout <10.0 | -1>]
 . start beacon.
@bps \
	install
 . install bps.
@bps \
	introspect \
	[~start_bluetooth,verbose,unique_bus_name=<1:234>]
 . introspect <1:234>.
@bps \
	receiver \
	[~start_bluetooth,verbose] \
	[--grep <sparrow>] \
	[--timeout <10>]
 . start receiver.
@bps \
	receiver \
	[~python,~start_bluetooth,verbose]
 . start receiver.
@bps \
	start_bluetooth \
	[verbose]
 . start bluetooth.
@bps \
	test \
	[~start_bluetooth,verbose]
 . d-bus ping test.
```
