from typing import Dict

from bluer_objects.README.consts import assets2

from bluer_sandbox.README.consts import ai4k_assets2

dict_of_experiments: Dict[str, Dict] = {
    "multimeter": {
        "marquee": f"{ai4k_assets2}/20251009_114411.jpg",
        "description": "batteries, AC, battery-bus w/ different lights + on charger, what else?",
    },
    "caliper": {
        "marquee": f"{ai4k_assets2}/20250616_112027.jpg",
        "description": "hair, paper, finger (what's wrong?), different sides of a spoon, what else?",
    },
    "ultrasonic": {
        "marquee": f"{assets2}/ultrasonic-sensor-tester/00.jpg?raw=true",
        "description": "tester, make sense of how it works, measure with one sensor, arzhang.",
    },
    "template": {
        "marquee": "template",
        "description": "",
    },
}
