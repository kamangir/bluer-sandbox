from bluer_ai.env import BLUER_AI_NATIONAL_INTERNAT_INDEX
from bluer_objects import objects

from bluer_sandbox.radar.fetch import fetch


def test_radar_fetch():
    object_name = objects.unique_object("test_radar_fetch")

    assert fetch(
        object_name=object_name,
        max_iteration=3,
    )
