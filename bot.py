import requests
import time

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def send_alert(message):
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(TELEGRAM_URL, data=payload)

    if response.status_code == 200:
        print("Alert sent successfully")
    else:
        print("Failed to send alert")


def monitor_event():
    events = [
        "Website status changed",
        "New lead added to CRM",
        "Price alert triggered",
        "Task completed successfully",
        "Inventory stock updated"
    ]

    for event in events:
        send_alert(f"Notification: {event}")
        time.sleep(2)


if __name__ == "__main__":
    monitor_event()
