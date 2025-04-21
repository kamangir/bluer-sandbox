# offline_llm

```bash
@offline_llm \
	build \
	[dryrun]
 . build offline_llm.
@offline_llm \
	chat \
	[download_model,tiny,~upload] \
	[-|<object-name>]
 . chat with offline_llm.
@plugin \
	create_env
 . create env.
@offline_llm \
	model \
	download \
	[dryrun,overwrite,tiny]
 . download the model.
@offline_llm \
	model \
	get \
	[filename | object_name | repo_name] \
	[tiny]
 . get model properties.
@offline_llm \
	prompt \
	[download_model,tiny,~upload] \
	"<prompt>" \
	[-|<object-name>]
 . "<prompt>" -> offline_llm.
```
