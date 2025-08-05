import pytest

from bluer_sandbox.interview.anagram import count_anagrams, count_anagrams_in_list

dictionary = [
    "hack",
    "a",
    "rank",
    "khac",
    "ackh",
    "kran",
    "rankhacker",
    "a",
    "ab",
    "ba",
    "stairs",
    "raits",
]

query = ["a", "nark", "bs", "hack", "stair"]

expected_output_list = [2, 2, 0, 3, 1]


@pytest.mark.parametrize(
    ["query_string", "expected_output"],
    [
        [word, expected_output]
        for word, expected_output in zip(query, expected_output_list)
    ],
)
def test_count_anagrams(
    query_string: str,
    expected_output: int,
):
    assert count_anagrams(dictionary, query_string) == expected_output


def test_count_anagrams_in_list():
    assert count_anagrams_in_list(dictionary, query) == expected_output_list
