import pytest

from bluer_sandbox.offline_llm.model.functions import get


@pytest.mark.parametrize(
    ["what", "is_valid"],
    [
        ["filename", True],
        ["object_name", True],
        ["repo_name", True],
        ["maker", False],
    ],
)
@pytest.mark.parametrize(
    ["tiny"],
    [
        [True],
        [False],
    ],
)
def test_offline_llm_model_get(
    what: str,
    tiny: bool,
    is_valid: bool,
):
    thing = get(what=what, tiny=tiny)

    assert thing

    if is_valid:
        assert "invalid" not in thing
    else:
        assert "invalid" in thing
