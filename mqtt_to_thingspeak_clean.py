import paho.mqtt.client as mqtt
import requests
import json

MQTT_BROKER = "mqtt.eclipseprojects.io"
MQTT_TOPIC = "iot/station/#"

THINGSPEAK_WRITE_API_KEY = "U6OLGDQVT6LIJW1M"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

def on_message(client, userdata, msg):
    try:
        print("📥 Message received from MQTT!")  # Debug print
        payload = msg.payload.decode()
        print(f"Payload: {payload}")
        data = json.loads(payload)

        temperature = data.get("temperature")
        humidity = data.get("humidity")
        co2 = data.get("co2")

        ts_payload = {
            "api_key": THINGSPEAK_WRITE_API_KEY,
            "field1": temperature,
            "field2": humidity,
            "field3": co2
        }

        response = requests.post(THINGSPEAK_URL, data=ts_payload)
        print(f"ThingSpeak Response: {response.text}")  # Debug print

        if response.status_code == 200:
            print("✅ Data sent to ThingSpeak!")
        else:
            print("❌ Failed to send:", response.text)
    except Exception as e:
        print("❌ Error:", e)

def main():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(MQTT_BROKER, 1883, 60)
    client.subscribe(MQTT_TOPIC)
    print("🔌 Subscribed to MQTT. Waiting for messages...\n")
    client.loop_forever()

if __name__ == "__main__":
    main()
