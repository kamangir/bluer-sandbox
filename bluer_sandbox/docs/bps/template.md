title:::

bluer-positioning system.

> A distributed, serverless positioning mesh where every Raspberry Pi acts as both a tag and a local estimator: each node continuously advertises a compact BLE packet containing its node ID, mobility flag, and its current best-estimate pose (x,y,σ,seq), and simultaneously scans for neighbor adverts to collect RSSI + neighbor poses. Anchors are marked static with known coordinates and low uncertainty; mobiles fuse anchors + neighbor pseudo-ranges (RSSI→distance, calibrated per site) with a lightweight weighted least-squares + EKF/Covariance-Intersection step, adapt advertising/scan rates when moving, and use short rolling HMAC tokens to prevent simple spoofing. The result is a gossiping swarm that converges locally to consistent positions, degrades gracefully to coarse proximity when RF is noisy, and can be migrated later to UWB without changing the peer-to-peer protocol.

items:::

- [AI convo](https://chatgpt.com/c/68e79d65-e938-8327-b1e1-2536f7b6fb41)
- [literature](./literature.md)
- [sandbox](../../../sandbox/bps)
- [bluer_sandbox.bps](../../bps)
- [test & introspect](./test-introspect.md)
- [beacon & receiver](./beacon-receiver.md)