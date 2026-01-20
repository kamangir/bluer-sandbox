from typing import Dict, List
from enum import Enum, auto
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from blueness import module
from bluer_options.logger.config import log_list
from bluer_objects import file
from bluer_objects import objects
from bluer_objects.metadata import post_to_object
from bluer_objects import file
from bluer_objects import objects

from bluer_sandbox.radar.functions import get_root
from bluer_sandbox import NAME
from bluer_sandbox.radar.hashing import hash_of
from bluer_sandbox.logger import logger


NAME = module.name(__file__, NAME)


class URLState(Enum):
    FOUND = auto()
    ACCESSED = auto()


class WebState:
    filename = "radar.dill"

    def __init__(
        self,
        object_name: str,
        roots: bool = True,
    ):
        self.object_name = object_name
        self.roots = roots

        self.dict_of_urls: Dict[str, URLState] = {}

        logger.info(
            "{}[{}{}]".format(
                self.__class__.__name__,
                self.object_name,
                ":roots" if self.roots else "",
            )
        )

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

    def fetch(
        self,
        url: str,
    ) -> bool:
        logger.info(
            "{}.fetch({})".format(
                self.__class__.__name__,
                url,
            )
        )

        success = False
        try:
            with urllib.request.urlopen(url) as response:
                content = response.read().decode("utf-8")
            soup = BeautifulSoup(content, "html.parser")

            list_of_urls = list({link.get("href") for link in soup.find_all("a")})
            list_of_urls = [
                url_
                for url_ in list_of_urls
                if isinstance(url_, str) and not url_.startswith("#")
            ]
            list_of_urls = [
                urljoin(url, url_) if url_.startswith("/") else url_
                for url_ in list_of_urls
            ]

            log_list(
                logger,
                "found",
                list_of_urls,
                "url(s)",
            )

            for url_ in sorted(list(set(list_of_urls))):
                self.append(url_, URLState.FOUND)

            filename = objects.path_of(
                object_name=self.object_name,
                filename="{}.html".format(hash_of(url)),
                create=True,
            )

            with open(filename, "w") as f:
                f.write(content)

            logger.info(f"{url} -> {filename}")

            success = True
        except Exception as e:
            logger.error(e)
            self.append(url, URLState.FOUND)

        if not success:
            return success

        self.append(url, URLState.ACCESSED)

        success = post_to_object(
            self.object_name,
            "radar",
            self.as_dict,
        )

        return success

    def load(self) -> bool:
        filename = objects.path_of(
            object_name=self.object_name,
            filename=self.filename,
        )

        if not file.exists(filename):
            logger.warning("no radar cache to load.")
            self.dict_of_urls = {}
            return True

        success, self.dict_of_urls = file.load(
            filename,
            ignore_error=True,
            default={},
        )

        return success

    @property
    def seed(self) -> str:
        candidates = [
            url for url, state in self.dict_of_urls.items() if state == URLState.FOUND
        ]
        output = candidates[0] if candidates else ""

        if output:
            logger.info(f"{self.__class__.__name__}.seed={output}")
        else:
            logger.info(f"no seed in {self.__class__.__name__}.")

        return output

    def save(
        self,
        log: bool = True,
    ) -> bool:
        return file.save(
            objects.path_of(
                object_name=self.object_name,
                filename=self.filename,
            ),
            self.dict_of_urls,
            log=log,
        )
