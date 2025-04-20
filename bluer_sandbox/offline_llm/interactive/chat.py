from blueness import module

from bluer_objects import objects

from bluer_sandbox import NAME
from bluer_sandbox.offline_llm.model.functions import get
from bluer_sandbox.offline_llm.interactive.interface import LlamaCppInterface
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)


def chat(
    tiny: bool = False,
    n_tokens: int = 300,
    temp: float = 0.7,
) -> bool:
    logger.info(
        "{}.chat: {}".format(
            NAME,
            "tiny, " if tiny else "",
        )
    )

    model_object_name = get("object_name", tiny=tiny)
    model_filename = get("filename", tiny=tiny)
    logger.info(f"model: {model_object_name}/{model_filename}")

    llama = LlamaCppInterface(
        model_path=objects.path_of(
            object_name=model_object_name,
            filename=model_filename,
        ),
        n_tokens=n_tokens,
        temp=temp,
    )

    llama.initialize()

    try:
        while True:
            user_input = input("\nYou: ")
            if user_input.strip().lower() == "quit":
                break

            response = llama.send_prompt(user_input)
            print(f"\nLlama: {response}")
    finally:
        llama.shutdown()

    return True
