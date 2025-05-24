import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_sandbox import NAME
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="void",
)
args = parser.parse_args()

success = False
if args.task == "void":
    success = False
else:
    success = None

sys_exit(logger, NAME, args.task, success)
