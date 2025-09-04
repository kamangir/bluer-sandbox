from typing import List

from blueness import module

from bluer_sandbox import NAME
from bluer_sandbox.village.family import Family
from bluer_sandbox.village.person import Person
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)


class Village:
    parents: List[Person] = []

    families: List[Family] = []

    def load(
        self,
        object_name: str,
        verbose: bool = False,
    ) -> bool:
        logger.info(f"{NAME}.load({object_name})")

        logger.info("🪄")

        return True
