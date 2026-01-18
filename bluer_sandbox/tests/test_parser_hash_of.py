import pytest

from bluer_sandbox.radar.hashing import hash_of


@pytest.mark.parametrize(
    [
        "input",
        "expected_output",
    ],
    [
        [
            "this is a test",
            "2e99758548972a8e8822ad47fa1017ff72f06f3ff6a016851f45c398732bc50c",
        ],
    ],
)
def test_parser_hash_of(
    input: str,
    expected_output: str,
):
    assert hash_of(input) == expected_output
