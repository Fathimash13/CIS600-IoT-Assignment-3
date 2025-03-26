import random
import time
import paho.mqtt.client as mqtt
import uuid
import json

STATION_ID = str(uuid.uuid4())[:8]
MQTT_BROKER = "mqtt.eclipseprojects.io"
MQTT_PORT = 1883
MQTT_TOPIC = f"iot/station/{STATION_ID}"

def generate_sensor_data():
    temperature = round(random.uniform(-50, 50), 2)
    humidity = round(random.uniform(0, 100), 2)
    co2 = random.randint(300, 2000)
    return temperature, humidity, co2

def main():
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    print("Station is sending data to MQTT...\n")

    try:
        for _ in range(10):
            temperature, humidity, co2 = generate_sensor_data()
            message = {
                "station_id": STATION_ID,
                "temperature": temperature,
                "humidity": humidity,
                "co2": co2
            }
            client.publish(MQTT_TOPIC, json.dumps(message))
            print(f"Published: {message}")
            time.sleep(2)
        print("Finished sending 10 messages.")
    except KeyboardInterrupt:
        print("Interrupted.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()
