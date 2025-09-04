import pytest

from bluer_sandbox.village.person import Person


@pytest.mark.parametrize(
    [
        "person",
        "expected_is_alive",
    ],
    [
        [
            Person(
                name="Arash",
            ),
            True,
        ],
        [
            Person(
                name="Arash",
                sex="male",
            ),
            True,
        ],
        [
            Person(
                name="Arash",
                sex="male",
                death=2035,
            ),
            False,
        ],
        [
            Person(
                name="Arash",
                sex="male",
                death=2015,
            ),
            False,
        ],
    ],
)
def test_village_person(
    person: Person,
    expected_is_alive: bool,
):
    assert isinstance(person.as_str(), str)

    assert person.is_alive == expected_is_alive
