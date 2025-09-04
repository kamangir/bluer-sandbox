from bluer_sandbox.village.family import Family
from bluer_sandbox.village.person import Person


def test_village_family_blank():
    family = Family()

    assert isinstance(family.as_str(), str)

    assert isinstance(family.as_str(verbose=False), str)

    assert isinstance(family.as_str(verbose=True), str)


def test_village_family_no_children():
    family = Family()

    family.persons = [
        Person(
            name="Arash",
            sex="male",
        ),
        Person(
            name="Arash",
            sex="male",
            death=2035,
        ),
    ]

    assert isinstance(family.as_str(), str)

    assert isinstance(family.as_str(verbose=False), str)

    assert isinstance(family.as_str(verbose=True), str)


def test_village_family_with_children():
    family = Family()

    family.persons = [
        Person(
            name="Arash",
            sex="male",
        ),
        Person(
            name="Arash",
            sex="male",
            death=2035,
        ),
    ]

    family.children = [
        Person(
            name="Arash",
        ),
        Person(
            name="Arash",
            sex="male",
        ),
        Person(
            name="Arash",
            sex="male",
            death=2035,
        ),
    ]

    assert isinstance(family.as_str(), str)

    assert isinstance(family.as_str(verbose=False), str)

    assert isinstance(family.as_str(verbose=True), str)
