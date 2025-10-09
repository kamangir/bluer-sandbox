from bluer_sandbox.ai4k.experiments import dict_of_experiments

docs = [
    {
        "path": "../docs/ai4k",
        "macros": {
            "list:::": sorted(
                [
                    "1. [{experiment_name}](./{experiment_name}.md).".format(
                        experiment_name=experiment_name
                    )
                    for experiment_name in dict_of_experiments
                ]
            ),
        },
    },
] + [
    {
        "path": f"../docs/ai4k/{experiment_name}.md",
        "marquee": info.get("marquee", ""),
    }
    for experiment_name, info in dict_of_experiments.items()
    if experiment_name != "template"
]
