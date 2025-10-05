# aliases: assets

asset management in [github/kamangir/assets](https://github.com/kamangir/assets).

```bash
@assets \
	cd \
	[create,vol=<2>] \
	[<path>]
 . cd assets volume.
@assets \
	publish \
	[download,extensions=png+txt,~pull,push] \
	[.|<object-name>] \
	[--asset_name <other-object-name>] \
	[--prefix <prefix>]
 . <object-name>/<prefix> -> assets.
```
