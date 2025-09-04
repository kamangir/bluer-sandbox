import pytest

from bluer_objects import storage

from bluer_sandbox import env


@pytest.fixture
def test_village():
    assert storage.download(env.BLUER_VILLAGE_TEST_OBJECT)
