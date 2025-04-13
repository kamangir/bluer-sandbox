# offline_llm

```bash
@offline_llm \
	install \
	[dryrun]
 . install offline_llm.
@offline_llm \
	prompt \
	[~upload] \
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
