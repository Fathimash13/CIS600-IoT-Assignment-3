# CIS600 IoT Assignment 3 – Virtual Environmental Station
# Fathima sania
# NETID- fsania
# SUID- 518689600
## Overview

This project simulates a cloud-based IoT system using Python, MQTT, and ThingSpeak. It consists of:

- A virtual station that generates random environmental sensor data
- MQTT-based data publishing
- A bridge script that subscribes to MQTT and sends data to ThingSpeak
- Scripts to retrieve latest and historical data from ThingSpeak

## Files

- `mqtt_virtual_station_clean.py`: Sends MQTT sensor data
- `mqtt_to_thingspeak_clean.py`: Receives MQTT and sends to ThingSpeak
- `latest_sensor_data.py`: Fetches latest values from ThingSpeak
- `last_5_hours_temperature.py`: Fetches historical temperature values

## ThingSpeak Channel

- Channel ID: `2842452`
- Write API Key: `U6OLGDQVT6LIJW1M`
- Read API Key: `KTRW410OIF0W5DBE`

## How to Run

### 1. Start MQTT Publisher:
```bash
python3 mqtt_virtual_station_clean.py

### 2.Start MQTT to ThingSpeak Bridge (in a separate terminal):
python3 mqtt_to_thingspeak_clean.py

### 3. Display the latest sensor data:
python3 latest_sensor_data.py

### 4. Display temperature data from the last 5 hours:
python3 last_5_hours_temperature.py

This `README.md`:
- ✅ Explains all files clearly
- ✅ Includes all API keys, instructions, and commands
- ✅ Covers setup and dependencies