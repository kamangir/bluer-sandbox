title:::

description:::


details::: bats vs. arzhang


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
details:::

items:::

[AI convo](https://chatgpt.com/c/68eb90c3-fd94-8332-ab1b-2b45871b2c3a)