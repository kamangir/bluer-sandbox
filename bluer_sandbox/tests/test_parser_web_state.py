import pytest

from bluer_sandbox.parser.classes import WebState, URLState


@pytest.mark.parametrize(
    ["roots"],
    [
        [True],
        [False],
    ],
)
def test_parser_web_state(roots: bool):
    state = WebState(roots=roots)

    assert isinstance(state.dict_of_urls, dict)

    state.append("https://google.com", URLState.FOUND)
    state.append("https://arvancloud.ir", URLState.ACCESSED)

    assert len(state.dict_of_urls) == 2
