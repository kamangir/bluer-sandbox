from bluer_objects import objects
from bluer_ai.env import abcli_is_github_workflow

from bluer_sandbox.parser.url import parse


def test_parser_parse():
    url = "https://cnn.com" if abcli_is_github_workflow else "https://iribnews.ir"

    object_name = objects.unique_object("test_parser_parse")

    success, list_of_urls = parse(
        url=url,
        object_name=object_name,
    )

    assert isinstance(success, bool)
    assert success
    assert isinstance(list_of_urls, list)
