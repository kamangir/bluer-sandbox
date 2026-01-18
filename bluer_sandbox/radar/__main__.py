import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_sandbox import NAME
from bluer_sandbox.radar.fetch import fetch_url
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="fetch",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--filename",
    type=str,
    default="",
)
parser.add_argument(
    "--url",
    type=str,
)
parser.add_argument(
    "--roots",
    type=int,
    default=1,
    help="0 | 1",
)
parser.add_argument(
    "--depth",
    type=int,
    default=1,
)
args = parser.parse_args()

success = False
if args.task == "fetch":
    success, _ = fetch_url(
        url=args.url,
        object_name=args.object_name,
        filename=args.filename,
        roots=args.roots == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
