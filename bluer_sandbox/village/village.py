from typing import List

from blueness import module
from bluer_options.logger import log_list
from bluer_objects import file, objects
from bluer_objects.metadata import get_from_object

from bluer_sandbox import NAME
from bluer_sandbox.village.family import Family
from bluer_sandbox.village.person import Person
from bluer_sandbox.logger import logger

NAME = module.name(__file__, NAME)


class Village:
    persons: List[Person] = []

    families: List[Family] = []

    def load(
        self,
        object_name: str,
        verbose: bool = False,
    ) -> bool:
        logger.info(f"{NAME}.load({object_name})")

        persons = get_from_object(object_name, "persons")
        self.persons = [
            Person(
                name=person_.get("name", "unknown"),
                sex=person_.get("sex", "female"),
                death=person_.get("death", -1),
            )
            for person_ in persons
        ]
        if verbose:
            log_list(
                logger,
                "loaded",
                [person.as_str() for person in self.persons],
                "person(s)",
            )
        else:
            logger.info(f"loaded {len(self.persons)} person(s).")

        families = get_from_object(object_name, "families")

        logger.info("🪄")

        return True
