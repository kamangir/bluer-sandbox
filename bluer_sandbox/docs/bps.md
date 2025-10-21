# bps

bluer-positioning system.

> A distributed, serverless positioning mesh where every Raspberry Pi acts as both a tag and a local estimator: each node continuously advertises a compact BLE packet containing its node ID, mobility flag, and its current best-estimate pose (x,y,σ,seq), and simultaneously scans for neighbor adverts to collect RSSI + neighbor poses. Anchors are marked static with known coordinates and low uncertainty; mobiles fuse anchors + neighbor pseudo-ranges (RSSI→distance, calibrated per site) with a lightweight weighted least-squares + EKF/Covariance-Intersection step, adapt advertising/scan rates when moving, and use short rolling HMAC tokens to prevent simple spoofing. The result is a gossiping swarm that converges locally to consistent positions, degrades gracefully to coarse proximity when RF is noisy, and can be migrated later to UWB without changing the peer-to-peer protocol.

|   |   |   |
| --- | --- | --- |
| [![image](https://github.com/kamangir/assets2/raw/main/bps/01.png?raw=true)](https://github.com/kamangir/assets2/raw/main/bps/01.png?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/bps/02.png?raw=true)](https://github.com/kamangir/assets2/raw/main/bps/02.png?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/bps/03.png?raw=true)](https://github.com/kamangir/assets2/raw/main/bps/03.png?raw=true) |

[AI convo](https://chatgpt.com/c/68e79d65-e938-8327-b1e1-2536f7b6fb41)

## literature

- [Research Progress of Wireless Positioning Methods Based on RSSI](https://www.mdpi.com/2079-9292/13/2/360) - 2024

> A modern survey of RSSI-based positioning techniques across BLE, Wi-Fi, ZigBee, and 5G.
It explains theoretical limitations of RSSI (path-loss variability, multipath fading) and outlines correction strategies.

- [Bluetooth indoor positioning system based on improved RSSI data](https://www.researchgate.net/publication/381412475_Bluetooth_indoor_positioning_system_based_on_improved_RSSI_data) - 2024

- [Peer-To-Peer UWB Ranges as a Source of Training Data for Estimating BLE RSSI Path-Loss Exponents](https://ceur-ws.org/Vol-3248/paper15.pdf) - 2022

> Proposes using precise UWB peer-to-peer ranges to calibrate BLE path-loss parameters automatically. Shows how multi-modal measurements improve BLE localization accuracy by up to 40%.

- [A Survey of Robot Swarms’ Relative Localization Methods](https://www.mdpi.com/1424-8220/22/12/4424) - 2022

> A comprehensive review of how robot swarms estimate relative positions using sensors such as BLE, UWB, infrared, and vision. It categorizes algorithms by communication type, sensing range, and scalability.

- [From Robot Self‑Localization to Global‑Localization: An RSSI Based Approach” (ArXiv)](https://arxiv.org/abs/2112.10578) - 2021

> presents a **simulation-based** method for enabling groups of mobile robots to localize themselves in GPS-denied environments. Some robots act as fixed beacons, broadcasting signals whose received strength (RSSI) is used by other robots to estimate their global position **through geometric reconstruction**. The approach was tested only in simulation (Webots) and not on physical robots. Reported average errors were about 0.6 m with 10 % Gaussian noise, 1.4 m with 20 % noise, and ≈0.1 m in near-ideal short-range conditions (3–3.5 m from beacons); within about 6 m of beacons, the total error remained under 1 m.

- [Bluetooth Low Energy Technology Applied to Indoor Positioning Systems: An Overview](https://ceur-ws.org/Vol-3248/paper15.pdf) - 2020

- [RSSI Filtering Methods Applied to Localization using Bluetooth Low Energy](https://www.researchgate.net/publication/363649251_RSSI_Filtering_Methods_Applied_to_Localization_using_Bluetooth_Low_Energy) - 2020

> Focuses on the signal-processing side of BLE localization. It evaluates Kalman filters, moving averages, and histogram-based smoothing to mitigate RSSI noise.

- [Indoor localization using radio beacon technology](https://www.researchgate.net/publication/329840131_Indoor_localization_using_radio_beacon_technology) - 2018
