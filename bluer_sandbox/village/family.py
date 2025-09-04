from typing import List

from bluer_sandbox.village.person import Person


class Family:
    def __init__(self):
        self.persons: List[Person] = []
        self.children: List[Person] = []

    def as_str(
        self,
        verbose: bool = True,
    ) -> str:
        return "[{}]{}".format(
            " + ".join(
                [person.as_str() if verbose else person.name for person in self.persons]
            ),
            (
                ""
                if not self.children
                else " -> {}".format(
                    " + ".join(
                        [
                            child.as_str() if verbose else child.name
                            for child in self.children
                        ]
                    )
                )
            ),
        )
