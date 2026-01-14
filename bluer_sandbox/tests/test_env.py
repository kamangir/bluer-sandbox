from bluer_options.testing import are_nonempty_strs
from bluer_ai.tests.test_env import test_bluer_ai_env
from bluer_objects.tests.test_env import test_bluer_objects_env

from bluer_sandbox import env


def test_required_env():
    test_bluer_ai_env()
    test_bluer_objects_env()


def test_bluer_sandbox_env():
    assert are_nonempty_strs(
        [
            env.ARVANCLOUD_PRIVATE_KEY,
            env.BLUER_SANDBOX_GREEN_OBJECT_NAME,
            env.BLUER_SANDBOX_V2RAY_TEST_VLESS,
            env.BLUER_VILLAGE_OBJECT,
            env.BLUER_VILLAGE_TEST_OBJECT,
        ]
    )
