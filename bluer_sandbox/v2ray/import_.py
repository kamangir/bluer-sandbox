from blueness import module

from bluer_objects import file, objects

from bluer_sandbox import NAME
from bluer_sandbox.logger import logger


NAME = module.name(__file__, NAME)


def complete(
    object_name: str,
) -> bool:
    logger.info(f"{NAME}.complete: {object_name}")

    filename = objects.path_of(
        object_name=object_name,
        filename="config.json",
    )

    success, config = file.load_json(filename)
    if not success:
        return success

    config["inbounds"] = [
        {
            "port": 8080,
            "listen": "127.0.0.1",
            "protocol": "http",
            "settings": {},
        }
    ]

    return file.save_json(
        filename,
        config,
        log=True,
    )
