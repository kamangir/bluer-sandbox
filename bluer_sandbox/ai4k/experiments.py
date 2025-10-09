from typing import Dict

from bluer_objects.README.consts import assets2

from bluer_sandbox.README.consts import ai4k_assets2

dict_of_experiments: Dict[str, Dict] = {
    "multimeter": {
        "marquee": f"{ai4k_assets2}/20251009_114411.jpg",
        "description": "batteries, AC, battery-bus w/ different lights + on charger, what else?",
        "doc": "TBA",
        "pdf": "TBA",
    },
    "caliper": {
        "marquee": f"{ai4k_assets2}/20250616_112027.jpg",
        "description": "hair, paper, finger (what's wrong?), different sides of a spoon, what else?",
        "doc": "TBA",
        "pdf": "TBA",
    },
    "ultrasonic": {
        "marquee": f"{assets2}/ultrasonic-sensor-tester/00.jpg?raw=true",
        "description": "[ultrasonic sensor tester](https://github.com/kamangir/bluer-sbc/blob/main/bluer_sbc/docs/ultrasonic-sensor-tester.md), make sense of how it works, measure with one sensor, [arzhang](https://github.com/kamangir/bluer-ugv/tree/main/bluer_ugv/docs/arzhang).",
        "doc": "https://docs.google.com/document/d/1reuY9N9Aaf6adRIOKOe7NaPj7R-4J7XVQflDrQKl4uM/edit?usp=sharing",
        "pdf": "TBA",
    },
    "template": {
        "marquee": "template",
        "description": "",
        "doc": "TBA",
        "pdf": "TBA",
    },
}
