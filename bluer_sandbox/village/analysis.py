from blueness import module

from bluer_plugin import NAME
from bluer_plugin.logger import logger


NAME = module.name(__file__, NAME)


def analyze(
    object_name: str,
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.analyze: {object_name}")

    logger.info("🪄")

    return True
