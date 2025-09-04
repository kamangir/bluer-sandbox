from bluer_objects import storage

from bluer_sandbox import env
from bluer_sandbox.tests.village import test_village
from bluer_sandbox.village.analysis import analyze


def test_village_analyze(test_village):
    assert analyze(
        object_name=env.BLUER_VILLAGE_TEST_OBJECT,
        verbose=1,
    )
