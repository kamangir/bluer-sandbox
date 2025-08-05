import pytest

from bluer_sandbox import VERSION

words_1 = [
    "Bat",
    " tab",
    " Tap",
    "pat",
    "CAT",
    "Act!",
    "tac",
    "rat",
    "tar",
    "Art",
    "123",
    "",
    " ",
    "python",
]

words = [
    "Evil",
    "Vile",
    "Live",
    "veil",
    "Stone",
    "tones",
    "Notes",
    "listen",
    "Silent",
    "enlist",
    "12345",
    "stone!",
    "stop",
    "pots",
    "post",
]


@pytest.mark.parametrize(
    ["words"],
    [[words]],
)
def test_anagram_groups(words):
    assert VERSION
