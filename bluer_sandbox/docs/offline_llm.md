# offline-llm

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


```yaml
output:
- ' Why is Mathematics said to be the Voice of God?'
- Mathematics is often said to be the voice of God because it is a universal language
  that can be used to understand and communicate complex ideas. It is a logical and
  precise system that can be used to describe and analyze the natural world, and it
  has been used to make many important discoveries and predictions about the universe.
- One of the reasons why mathematics is considered to be the voice of God is that
  it is based on principles of logic and reason that are independent of any particular
  culture or language. This means that anyone who is willing to learn and understand
  it can use it to communicate with others, regardless of their background or location.
- Another reason why mathematics is considered to be the voice of God is that it is
  a powerful tool for understanding and predicting the behavior of natural systems.
  For example, it has been used to make predictions about the weather, the movement
  of celestial bodies, and the spread of diseases.
- Overall, the idea that mathematics is the voice of God reflects the belief that
  it is a powerful and meaningful language that can be used to understand and communicate
  important ideas about the world and our place in it. [end of text]
prompt:
- Why is Mathematics said to be the Voice of God?

```
