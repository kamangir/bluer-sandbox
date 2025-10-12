from bluer_objects.README.items import Items_of_dict, list_of_dict, ImageItems

from bluer_sandbox.ai4k.experiments import dict_of_experiments

docs = [
    {
        "path": "../docs/ai4k",
    },
    {
        "path": "../docs/ai4k/sessions.md",
    },
    {
        "path": "../docs/ai4k/experiments.md",
        "items": Items_of_dict(dict_of_experiments),
        "cols": 2,
        "macros": {
            "list:::": list_of_dict(dict_of_experiments),
        },
    },
] + [
    {
        "path": f"../docs/ai4k/experiments/{experiment_name}.md",
        "cols": info.get("cols", 3),
        "items": ImageItems(
            {
                info.get("marquee", ""): "",
                **info.get("items", {}),
            }
        ),
        "macros": {
            "description:::": [f"- {item}" for item in info["description"]],
        },
    }
    for experiment_name, info in dict_of_experiments.items()
    if experiment_name != "template"
]
