import argparse

from blueness import module
from blueness.argparse.generic import sys_exit
from bluer_ai.env import BLUER_AI_NATIONAL_INTERNAT_INDEX

from bluer_sandbox import NAME
from bluer_sandbox.radar.classes import WebState, URLState
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="fetch",
)
parser.add_argument(
    "--depth",
    type=int,
    default=1,
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--roots",
    type=int,
    default=1,
    help="0 | 1",
)
parser.add_argument(
    "--seed",
    type=str,
    default="",
)
args = parser.parse_args()

success = False
if args.task == "fetch":
    state = WebState(
        object_name=args.object_name,
        roots=args.roots == 1,
    )

    success = state.load()

    if success:
        seed: str = state.seed
        if not seed:
            seed = args.seed
        if not seed:
            seed = BLUER_AI_NATIONAL_INTERNAT_INDEX
        logger.info(f"seed: {seed}")

        success = state.fetch(url=seed)

    if success:
        success = state.save()
else:
    success = None

sys_exit(logger, NAME, args.task, success)
