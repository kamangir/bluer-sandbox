import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_sandbox import NAME
from bluer_sandbox import env
from bluer_sandbox.green.db import GreenDB
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="review",
)
parser.add_argument(
    "--object_name",
    type=str,
    default=env.BLUER_SANDBOX_GREEN_OBJECT_NAME,
)
parser.add_argument(
    "--log",
    type=bool,
    default=1,
    help="0|1",
)

args = parser.parse_args()

success = False
if args.task == "review":
    db = GreenDB(object_name=args.object_name)
    success = db.review(log=args.log == 1)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
