import pytest

from bluer_objects import objects

from bluer_sandbox.parser.parsing import parse


@pytest.mark.parametrize(
    ["url"],
    [
        ["https://iribnews.ir"],
    ],
)
def test_parser_parse(url: str):
    object_name = objects.unique_object("test_parser_parse")

    success, list_of_urls = parse(
        url=url,
        object_name=object_name,
    )

    assert isinstance(success, bool)
    assert isinstance(list_of_urls, list)
