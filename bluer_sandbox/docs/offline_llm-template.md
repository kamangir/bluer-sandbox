title:::

- using [llama.cpp](https://github.com/ggerganov/llama.cpp).
- [@llm](./aliases/llm.md)

```bash
@llm build
```

```bash
@select llm-$(@@timestamp)

@llm prompt download_model \
    "Why is Mathematics said to be the Voice of God?" .
```

set:::object_name offline_llm-2025-04-19-mojo58

metadata:::get:::object_name:::post_process