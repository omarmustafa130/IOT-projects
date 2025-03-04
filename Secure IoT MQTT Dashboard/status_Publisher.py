import paho.mqtt.client as mqtt
import time
from dotenv import load_dotenv
import os

load_dotenv()

LOCAL_BROKER = os.getenv("LOCAL_BROKER")
LOCAL_USERNAME = os.getenv("LOCAL_USERNAME")
LOCAL_PASSWORD = os.getenv("LOCAL_PASSWORD")
LOCAL_PORT = 1883

REMOTE_BROKER = os.getenv("REMOTE_BROKER")
REMOTE_USERNAME = os.getenv("REMOTE_USERNAME")
REMOTE_PASSWORD = os.getenv("REMOTE_PASSWD")
REMOTE_PORT = 1883
TOPIC = "/device/status"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(LOCAL_USERNAME, LOCAL_PASSWORD)
client.will_set(TOPIC, "offline", qos=1, retain=True)
client.connect(LOCAL_BROKER, LOCAL_PORT)

client.publish(TOPIC, "online", qos=1, retain=True)

print("Device is online. Press CTRL+C to stop...")
try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("Disconnecting...")
    client.disconnect()
