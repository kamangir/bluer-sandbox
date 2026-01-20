from bluer_ai.env import BLUER_AI_NATIONAL_INTERNAT_INDEX
from bluer_objects import objects

from bluer_sandbox.radar.classes import WebState


def test_radar_web_state_fetch():
    object_name = objects.unique_object("test_radar_web_state_fetch")

    state = WebState(object_name=object_name)

    assert state.fetch(url=BLUER_AI_NATIONAL_INTERNAT_INDEX)
