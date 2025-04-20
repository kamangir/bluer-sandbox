# offline_llm

```bash
@offline_llm \
	install \
	[dryrun]
 . install offline_llm.
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

```bash
@offline_llm install
```

```bash
@select offline_llm-$(@@timestamp)

@offline_llm prompt - \
    "what is 2 ^ 7 + 11?" .
```


```yaml
output:
- ' what is 2 ^ 7 + 11?'
- 'A: 129 [end of text]'
prompt:
- what is 2 ^ 7 + 11?

```
