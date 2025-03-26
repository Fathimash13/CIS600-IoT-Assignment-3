import requests
import datetime

CHANNEL_ID = "2842452"
READ_API_KEY = "KTRW410OIF0W5DBE"
SENSOR_FIELD = "1"  # field1 = temperature

# Get time 5 hours ago in UTC format
end_time = datetime.datetime.utcnow()
start_time = end_time - datetime.timedelta(hours=5)

URL = (
    f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/{SENSOR_FIELD}.json"
    f"?api_key={READ_API_KEY}&start={start_time.isoformat()}Z&end={end_time.isoformat()}Z"
)

def main():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print("🌡️ Temperature Readings in the Last 5 Hours:")
        for feed in data["feeds"]:
            print(f"{feed['created_at']} -> {feed['field1']} °C")
    else:
        print("❌ Failed to fetch data:", response.text)

if __name__ == "__main__":
    main()
