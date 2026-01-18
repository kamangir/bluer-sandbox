import pytest

from bluer_objects import objects
from bluer_ai import env

from bluer_sandbox.parser.url import parse_url
from bluer_sandbox.parser.classes import WebState


@pytest.mark.parametrize(
    ["url"],
    [[env.BLUER_AI_NATIONAL_INTERNAT_INDEX]],
)
@pytest.mark.parametrize(
    ["roots"],
    [[True], [False]],
)
def test_parser_parse(
    url: str,
    roots: bool,
):
    object_name = objects.unique_object("test_parser_parse")

    success, state = parse_url(
        url=url,
        object_name=object_name,
        roots=roots,
    )

    assert isinstance(success, bool)
    assert success
    assert isinstance(state, WebState)

    assert isinstance(state.as_dict, dict)
