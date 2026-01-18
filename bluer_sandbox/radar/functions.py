import os
from typing import Tuple

from bluer_sandbox.logger import logger


def get_root(url: str) -> Tuple[bool, str]:
    prefix: str = ""
    url_root: str = ""
    for prefix_ in ["http://", "https://"]:
        if url.startswith(prefix_):
            url_root = url.split(prefix_, 1)[1]
            prefix = prefix_
            break

    if not url_root:
        logger.warning(f"bad url ignored: {url}")
        return False, ""

    if url_root.startswith("www."):
        url_root = url_root.split("www.", 1)[1]

    if os.sep in url_root:
        url_root = url_root.split(os.sep, 1)[0]

    if not url_root:
        logger.warning(f"bad url ignored: {url}")
        return False, ""

    url_root = f"{prefix}{url_root}"

    return True, url_root
