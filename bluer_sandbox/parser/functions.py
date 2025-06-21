from typing import Tuple, List
import urllib.request
from bs4 import BeautifulSoup
import re

from blueness import module
from bluer_objects import objects

from bluer_sandbox import NAME
from bluer_sandbox.logger import logger


NAME = module.name(__file__, NAME)


def parse(
    url: str,
    object_name: str = "",
    filename: str = "",
) -> Tuple[bool, List[str]]:
    logger.info("{}.parse({})".format(NAME, url))

    success = False
    list_of_urls: List[str] = []

    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode("utf-8")
        soup = BeautifulSoup(content, "html.parser")

        list_of_urls = [
            href
            for href in [link.get("href") for link in soup.find_all("a")]
            if re.match(r"^https?://", href)
        ]

        if object_name:
            if not filename:
                filename = re.sub(r"[^\w\s]", "_", url) + ".html"

            with open(
                filename,
                "w",
            ) as f:
                f.write(content)

            logger.info(f"-> {filename}")

        success = True
    except Exception as e:
        logger.error(e)

    return success, list_of_urls
