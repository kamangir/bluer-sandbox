from bluer_sandbox.village.person import Person


def test_village_person():
    person = Person(
        name="Arash",
    )

    person = Person(
        name="Arash",
        sex="male",
    )

    person = Person(
        name="Arash",
        sex="male",
        death=2035,
    )

    assert isinstance(person.as_str(), str)
