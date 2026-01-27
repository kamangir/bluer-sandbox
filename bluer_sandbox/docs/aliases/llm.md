# aliases: llm

```bash
@llm \
	build \
	[dryrun]
 . build llm.
@llm \
	chat \
	[download_model,tiny,~upload] \
	[-|<object-name>]
 . chat with llm.
@plugin \
	create_env
 . create env.
@llm \
	model \
	download \
	[dryrun,overwrite,tiny]
 . download the model.
@llm \
	model \
	get \
	[filename | object_name | repo_name] \
	[tiny]
 . get model properties.
@llm \
	prompt \
	[download_model,tiny,upload] \
	"<prompt>" \
	[-|<object-name>]
 . "<prompt>" -> llm.
```
