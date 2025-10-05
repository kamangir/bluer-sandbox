# aliases: assets

asset management in [github/kamangir/assets](https://github.com/kamangir/assets), and its volumes: [2](https://github.com/kamangir/assets2).

```bash
@assets \
	cd \
	[create,vol=<2>] \
	[<path>]
 . cd assets volume.
@assets \
	mv \
	[create,extension=<png>,vol=<2>] \
	[<path>] \
	[push,browse,~increment_version,offline,~status]
 . mv assets to volume.
@assets \
	publish \
	[download,extensions=<png+txt>,~pull,push] \
	[.|<object-name>] \
	[--asset_name <other-object-name>] \
	[--prefix <prefix>]
 . <object-name>/<prefix> -> assets.
```
