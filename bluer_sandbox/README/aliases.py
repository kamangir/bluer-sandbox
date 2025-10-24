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
        "docker",
        "notebooks",
        "offline_llm",
        "speedtest",
        "tor",
        "village",
    ]
]
