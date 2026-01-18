from typing import Tuple
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from blueness import module
from bluer_options.logger.config import log_list
from bluer_objects import file
from bluer_objects import objects
from bluer_objects import path
from bluer_objects.metadata import post_to_object

from bluer_sandbox import NAME
from bluer_sandbox.radar.hashing import hash_of
from bluer_sandbox.radar.classes import WebState, URLState
from bluer_sandbox.logger import logger


NAME = module.name(__file__, NAME)


def fetch_url(
    url: str,
    object_name: str = "",
    filename: str = "",
    roots: bool = True,
) -> Tuple[bool, WebState]:
    logger.info(
        "{}.fetch_url{}: {}{}".format(
            NAME,
            "[roots]" if roots else "",
            url,
            f"-> {filename}" if filename else "",
        )
    )

    output = WebState(roots=roots)

    success = False
    try:
        response = urllib.request.urlopen(url)
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
            output.append(url_, URLState.FOUND)

        if object_name:
            if not filename:
                filename = "cache/{}.html".format(hash_of(url))

            filename = objects.path_of(
                object_name=object_name,
                filename=filename,
                create=True,
            )

            if not path.create(file.path(filename)):
                return False

            with open(filename, "w") as f:
                f.write(content)

            logger.info(f"{url} -> {filename}")

        success = True
    except Exception as e:
        logger.error(e)
        output.append(url, URLState.FOUND)

    if not success:
        return success, output

    output.append(url, URLState.ACCESSED)

    success = post_to_object(
        object_name,
        "parser",
        output.as_dict,
    )

    return success, output
