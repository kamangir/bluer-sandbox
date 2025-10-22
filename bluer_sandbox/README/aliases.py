docs = [
    {
        "path": "../docs/aliases",
    },
] + [
    {
        "path": f"../docs/aliases/{alias}.md",
    }
    for alias in [
        "arvancloud",
        "bps",
        "docker",
        "notebooks",
        "offline_llm",
        "speedtest",
        "tor",
        "village",
    ]
]
