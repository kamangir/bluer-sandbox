from bluer_objects.README.items import Items_of_dict, list_of_dict

from bluer_sandbox.ai4k.experiments import dict_of_experiments

docs = [
    {
        "path": "../docs/ai4k",
        "items": Items_of_dict(dict_of_experiments),
        "macros": {
            "list:::": list_of_dict(dict_of_experiments),
        },
    },
] + [
    {
        "path": f"../docs/ai4k/{experiment_name}.md",
        "marquee": info.get("marquee", ""),
        "macros": {
            "description:::": [info["description"]],
        },
    }
    for experiment_name, info in dict_of_experiments.items()
    if experiment_name != "template"
]
