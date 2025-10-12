# ai4k: ultrasonic

- watching the film [Here's What Bat Echolocation Sounds Like, Slowed Down](https://youtu.be/qJOloliWvB8?si=_lzHkcyTP0B1S7Ba).work with the [ultrasonic sensor tester](https://github.com/kamangir/bluer-sbc/blob/main/bluer_sbc/docs/ultrasonic-sensor-tester.md), make sense of how it works, measure with one sensor.
- drive [arzhang](https://github.com/kamangir/bluer-ugv/tree/main/bluer_ugv/docs/arzhang) and measure how far from an obstacle it stops.



<details>
<summary> bats vs. arzhang</summary>



| **Feature** | **Bats (Biological Echolocation)** | [**Arzhang (UGV)**](https://github.com/kamangir/bluer-ugv/tree/main/bluer_ugv/docs/arzhang) |
| - | - | - |
| **Signal Source & Receiver** | Emits ultrasonic chirps and listens with highly tuned ears | Uses HC-SR04 ultrasonic modules for transmit and receive |
| **Processing Unit** | Brain computes echo delay, Doppler shift, and object shape | Raspberry Pi running the `bluer-ugv` AI stack processes echo data |
| **Frequency Range** | ~20 – 200 kHz, species-dependent | ~40 kHz (configurable per sensor) |
| **Range & Resolution** | Up to several meters, sub-millimeter precision | 5 – 300 cm effective range, ±5 mm resolution |
| **Purpose** | Navigation, hunting, and obstacle avoidance in darkness | Obstacle avoidance, wall following, and AI-guided movement |
| **Adaptability** | Dynamically adjusts chirp pattern and frequency to context | Adjusts sampling rate and response thresholds (`clear`, `warning`, `danger`) |
| **Output Representation** | Builds a spatial map in the brain for real-time flight control | Generates sensor-fusion maps for motion planning and LED feedback |
| **Design Principle** | Evolved biological system | Engineered biomimicry inspired by bats’ echolocation |

</details>


|   |   |
| --- | --- |
| [![image](https://github.com/kamangir/assets2/raw/main/ultrasonic-sensor-tester/00.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/ultrasonic-sensor-tester/00.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/arzhang/20251005_112250.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/arzhang/20251005_112250.jpg?raw=true) |
| [![image](https://github.com/kamangir/assets2/raw/main/arzhang/VID-20250830-WA0000~3_1.gif?raw=true)](https://github.com/kamangir/assets2/raw/main/arzhang/VID-20250830-WA0000~3_1.gif?raw=true) |  |

[AI convo](https://chatgpt.com/c/68eb90c3-fd94-8332-ab1b-2b45871b2c3a)
