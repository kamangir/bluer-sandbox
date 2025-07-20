# offline_llm

- using [llama.cpp](https://github.com/ggerganov/llama.cpp).
- [@offline_llm](./aliases/offline_llm.md)

```bash
@offline_llm build
```

```bash
@select offline_llm-$(@@timestamp)

@offline_llm prompt download_model \
    "Why is Mathematics said to be the Voice of God?" .
```

set:::object_name offline_llm-2025-04-19-mojo58

metadata:::get:::object_name:::post_process