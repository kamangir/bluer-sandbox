from typing import Dict, List
from enum import Enum, auto

from bluer_sandbox.parser.functions import get_root
from bluer_sandbox.logger import logger


class URLState(Enum):
    FOUND = auto()
    ACCESSED = auto()


class WebState:
    def __init__(
        self,
        roots: bool = True,
    ):
        self.dict_of_urls: Dict[str, URLState] = {}
        self.roots = roots

    def append(
        self,
        url: str,
        state: URLState,
    ) -> bool:
        if self.roots:
            success, url = get_root(url)
            if not success:
                return success

        if self.dict_of_urls.get(url, None) == state:
            return True

        self.dict_of_urls[url] = state

        logger.info(
            "{}: {}".format(
                url,
                state.name.lower(),
            )
        )

        return True

    @property
    def as_dict(self) -> Dict[str, List[str]]:
        return {
            **{
                state.name.lower(): [
                    url for url, state_ in self.dict_of_urls.items() if state_ == state
                ]
                for state in URLState
            },
            "roots": self.roots,
        }
