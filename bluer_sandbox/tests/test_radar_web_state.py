import pytest

from bluer_objects import objects

from bluer_sandbox.radar.classes import WebState, URLState


@pytest.mark.parametrize(
    ["roots"],
    [
        [True],
        [False],
    ],
)
def test_radar_web_state(roots: bool):
    object_name = objects.unique_object("test_radar_web_state")

    state = WebState(
        object_name=object_name,
        roots=roots,
    )

    assert isinstance(state.seed, str)
    assert state.seed == ""

    assert isinstance(state.dict_of_urls, dict)

    state.append("https://irna.ir", URLState.FOUND)
    state.append("https://arvancloud.ir", URLState.ACCESSED)

    assert len(state.dict_of_urls) == 2

    assert state.save()

    assert state.load()

    assert state.seed == "https://irna.ir"

    assert isinstance(state.as_dict, dict)
