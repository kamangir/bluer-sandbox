import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_sandbox import NAME
from bluer_sandbox.offline_llm.interactive.chat import chat
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="chat",
)
parser.add_argument(
    "--tiny",
    type=int,
    help="0 | 1",
    default=0,
)
args = parser.parse_args()

success = False
if args.task == "chat":
    success = chat(tiny=args.tiny == 1)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
