from blueness import module

from bluer_objects import objects

from bluer_sandbox import NAME
from bluer_sandbox.offline_llm.model.functions import get
from bluer_sandbox.offline_llm.interactive.interface import LlamaInterface
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)


def chat(tiny: bool = False) -> bool:
    logger.info(
        "{}.chat: {}".format(
            NAME,
            "tiny, " if tiny else "",
        )
    )

    model_object_name = get("object_name", tiny=tiny)
    model_filename = get("filename", tiny=tiny)
    logger.info(f"model: {model_object_name}/{model_filename}")

    logger.info("🪄")

    return True
