# aliases: bps

```bash
@bps \
	beacon \
	[~start_bluetooth]
 . start beacon.
@bps \
	beacon_and_receiver \
	[~start_bluetooth] \
	[--role beacon | receiver | both]
 . start beacon and/or receiver.
@bps \
	install
 . install bps.
@bps \
	introspect \
	[~start_bluetooth,unique_bus_name=<1:234>]
 . introspect <1:234>.
@bps \
	receiver \
	[~start_bluetooth]
 . start receiver.
@bps \
	start_bluetooth
 . start bluetooth.
@bps \
	test \
	[~start_bluetooth]
 . d-bus ping test.
```
