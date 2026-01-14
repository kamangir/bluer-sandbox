from typing import List, Dict
import matplotlib.pyplot as plt

from bluer_options.logger.config import log_list
from bluer_objects import objects
from bluer_objects import file
from bluer_objects.metadata import get_from_object, post_to_object
from bluer_objects.graphics.signature import justify_text

from bluer_sandbox.host import signature
from bluer_sandbox import env
from bluer_sandbox.logger import logger


class GreenDB:
    def __init__(
        self,
        object_name: str = env.BLUER_SANDBOX_GREEN_OBJECT_NAME,
        load=True,
    ):
        self.object_name: str = object_name
        self.raw: List[str, Dict] = []

        if load:
            self.load()

    def graph(
        self,
        what: str = "gr",
        log: bool = True,
        line_width: int = 80,
    ) -> bool:
        plt.figure(figsize=(10, 4))
        plt.plot(
            self.values("date"),
            self.values(what),
            marker="o",
            color="green",
        )
        plt.title(
            justify_text(
                " | ".join(
                    objects.signature(object_name=self.object_name) + self.signature()
                ),
                line_width=line_width,
                return_str=True,
            )
        )
        plt.xlabel(
            justify_text(
                " | ".join(["date"] + signature()),
                line_width=line_width,
                return_str=True,
            )
        )
        plt.ylabel(what)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        return file.save_fig(
            objects.path_of(
                object_name=self.object_name,
                filename=f"{what}.png",
            ),
            log=log,
        )

    def load(self):
        self.raw = get_from_object(
            self.object_name,
            "green_db",
            [],
        )

        if not isinstance(self.raw, list):
            logger.warning(f"list expected, {self.raw.__class__.__name__} found.")
            self.raw = []

        log_list(
            logger,
            "loaded",
            [str(thing) for thing in self.values("date")],
            "entry(s)",
            itemize=False,
        )

    def review(
        self,
        log: bool = False,
    ) -> bool:
        return self.graph(
            "gr",
            log=log,
        )

    def save(self) -> bool:
        return post_to_object(
            self.object_name,
            "green_db",
            self.raw,
        )

    def signature(self) -> List[str]:
        return [
            "{} entry(s)".format(len(self.raw)),
            "{} .. {}".format(
                min(self.values("date")),
                max(self.values("date")),
            ),
        ]

    def values(self, what: str) -> List:
        return [entry[what] for entry in self.raw]
