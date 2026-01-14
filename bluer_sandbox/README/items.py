from bluer_objects import README
from bluer_objects.README.consts import assets, assets2

items = README.Items(
    [
        {
            "name": "green",
            "description": "☘️ tracking green use.",
            "url": "./bluer_sandbox/docs/green.md",
        },
        {
            "name": "netcat",
            "description": "tools to work with netcat.",
            "url": "./bluer_sandbox/docs/netcat.md",
        },
        {
            "name": "v2ray",
            "description": "tools to work with [v2ray](https://en.wikipedia.org/wiki/V2Ray).",
            "marquee": f"{assets2}/v2ray/v2ray.png?raw=true",
            "url": "./bluer_sandbox/docs/v2ray.md",
        },
        {
            "name": "arvancloud",
            "description": "tools to work with [arvancloud](https://arvancloud.ir/).",
            "marquee": f"{assets}/arvancloud/arvancloud.png?raw=true",
            "url": "./bluer_sandbox/docs/arvancloud.md",
        },
        {
            "name": "tor",
            "description": "tools to work with [tor](https://www.torproject.org/).",
            "marquee": f"{assets}/tor/tor2.png?raw=true",
            "url": "./bluer_sandbox/docs/tor.md",
        },
        {
            "name": "offline LLM",
            "description": "using [llama.cpp](https://github.com/ggerganov/llama.cpp).",
            "marquee": "https://user-images.githubusercontent.com/1991296/230134379-7181e485-c521-4d23-a0d6-f7b3b61ba524.png",
            "url": "./bluer_sandbox/docs/offline_llm.md",
        },
        {
            "name": "bluer village",
            "description": "a bluer village.",
            "url": "./bluer_sandbox/docs/aliases/village.md",
        },
    ]
)
