from tqdm import tqdm

from blueness import module
from bluer_ai.env import BLUER_AI_NATIONAL_INTERNAT_INDEX

from bluer_sandbox import NAME
from bluer_sandbox.radar.classes import WebState, URLState
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)


def fetch(
    object_name: str,
    max_iteration: int = 1,
    roots: bool = True,
    seed: str = "",
) -> bool:
    logger.info(
        "{}.fetch{}({}){}{}".format(
            NAME,
            "[roots]" if roots else "",
            object_name,
            f"x{max_iteration}" if max_iteration > 1 else "",
            f" : {seed}" if seed else "",
        )
    )

    state = WebState(
        object_name=object_name,
        roots=roots,
    )

    if not state.load():
        return False

    for iteration in tqdm(range(1, max_iteration + 1)):
        seed_: str = ""
        if iteration == 1:
            seed_ = seed
            if not seed_:
                seed_ = BLUER_AI_NATIONAL_INTERNAT_INDEX
        else:
            seed_ = state.seed
        if not seed_:
            logger.warning("seed not found.")
            break
        logger.info(f"#{iteration} - seed: {seed_}")

        if not state.fetch(url=seed_):
            logger.warning(f"fetch failed: {seed_}")
            state.append(seed_, URLState.FAILED)

    return state.save()
