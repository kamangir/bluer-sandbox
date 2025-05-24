from bluer_ai.tests.test_env import test_bluer_ai_env
from bluer_objects.tests.test_env import test_bluer_objects_env

from bluer_sandbox import env


def test_required_env():
    test_bluer_ai_env()
    test_bluer_objects_env()


def test_bluer_sandbox_env():
    assert env.BLUER_SANDBOX_CONFIG

    assert env.ARVANCLOUD_IP
    assert env.ARVANCLOUD_PRIVATE_KEY
