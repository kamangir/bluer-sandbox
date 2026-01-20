import pytest

from bluer_ai import env

from bluer_sandbox.radar.functions import get_root


@pytest.mark.parametrize(
    [
        "url",
        "expected_root",
        "expected_success",
    ],
    [
        [
            env.BLUER_AI_NATIONAL_INTERNAT_INDEX,
            "https://zoomit.ir",
            True,
        ],
        [
            "https://this.that.com/which/what",
            "https://this.that.com",
            True,
        ],
        [
            "https://www.this.that.com/which/what",
            "https://this.that.com",
            True,
        ],
        [
            "https://www.this.that.com/",
            "https://this.that.com",
            True,
        ],
        [
            "https://www.this.that.com",
            "https://this.that.com",
            True,
        ],
        [
            "xyz://this.that.com/which/what",
            "",
            False,
        ],
        [
            "this.that.com/which/what",
            "",
            False,
        ],
        [
            "",
            "",
            False,
        ],
    ],
)
def test_radar_get_root(
    url: str,
    expected_root: str,
    expected_success: bool,
):
    success, root = get_root(url)
    assert success == expected_success, url

    if success:
        assert root == expected_root, url
