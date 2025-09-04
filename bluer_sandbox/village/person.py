from typing import UNION, NONE


class Person:
    name: str
    sex: str
    death: int

    def __init__(
        self,
        name: str,
        sex: str = "female",
        death: int = -1,
    ):
        self.name = name
        self.sex = sex
        self.death = death

    def as_str(
        self,
    ) -> str:
        return "{} ({}{})".format(
            self.name,
            self.sex,
            "" if self.death == -1 else f", death: {self.death}",
        )
