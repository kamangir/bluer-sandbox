import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_sandbox import NAME
from bluer_sandbox.v2ray.import_ import complete
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="complete_import",
)
parser.add_argument(
    "--object_name",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "complete_import":
    success = complete(args.object_name)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
