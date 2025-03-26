import requests

CHANNEL_ID = "2842452"
READ_API_KEY = "KTRW410OIF0W5DBE"
URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds/last.json?api_key={READ_API_KEY}"

def main():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print("📡 Latest Sensor Data:")
        print(f"Temperature: {data['field1']} °C")
        print(f"Humidity: {data['field2']} %")
        print(f"CO₂: {data['field3']} ppm")
    else:
        print("❌ Failed to fetch data:", response.text)

if __name__ == "__main__":
    main()
