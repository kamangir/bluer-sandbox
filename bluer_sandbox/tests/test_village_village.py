from bluer_sandbox.tests.village import test_village
from bluer_sandbox.village.village import Village
from bluer_sandbox.village.person import Person
from bluer_sandbox import env


def test_village_village(test_village):
    village = Village()

    assert village.load(
        object_name=env.BLUER_VILLAGE_TEST_OBJECT,
        verbose=True,
    )

    person = village.get_person("Ziba Googooli")
    assert isinstance(person, Person)

    person = village.get_person("Arash Abadpour")
    assert person is None

    person = village.get_person("Arash Abadpour", add=True)
    assert isinstance(person, Person)
