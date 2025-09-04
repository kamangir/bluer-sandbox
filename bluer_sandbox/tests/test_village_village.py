from bluer_sandbox.tests.village import test_village
from bluer_sandbox.village.village import Village
from bluer_sandbox import env


def test_village_village(test_village):
    village = Village()

    assert village.load(
        object_name=env.BLUER_VILLAGE_TEST_OBJECT,
        verbose=True,
    )
