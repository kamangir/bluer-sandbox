from blueness.pypi import setup

from bluer_sandbox import NAME, VERSION, DESCRIPTION, REPO_NAME

setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.assets",
        f"{NAME}.help",
        f"{NAME}.offline_llm",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            ".abcli/**/*.sh",
            "assets/*",
        ],
    },
)
