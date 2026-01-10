from bluer_objects.README.alias import list_of_aliases

from bluer_sandbox import NAME


docs = [
    {
        "path": "../docs/aliases",
    },
] + [
    {
        "path": f"../docs/aliases/{alias_name}.md",
    }
    for alias_name in list_of_aliases(
        NAME,
        as_markdown=False,
    )
]
