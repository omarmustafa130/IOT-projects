from pymongo import MongoClient
import paho.mqtt.client as mqtt
import time
from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = "mqtt_subscriber_1"


LOCAL_BROKER = os.getenv("LOCAL_BROKER")
LOCAL_USERNAME = os.getenv("LOCAL_USERNAME")
LOCAL_PASSWORD = os.getenv("LOCAL_PASSWORD")
LOCAL_PORT = 1883
TOPIC = "#"

def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(TOPIC, qos=0)  # Resubscribe if necessary
    else:
        print(f"Connection failed with code {rc}")


def on_message(client, userdata, msg):
    data = {"topic": msg.topic, "value": msg.payload.decode()}
    print(f"📩 Received: {data}")


def on_disconnect(client, userdata, rc):
    print(f"Disconnected with code {rc}, reconnecting...")
    client.reconnect()

client = mqtt.Client(client_id=CLIENT_ID, clean_session=False, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(LOCAL_USERNAME, LOCAL_PASSWORD)
client.connect(LOCAL_BROKER, LOCAL_PORT, keepalive=300)  # Set to 5 minutes
client.on_connect = on_connect

client.on_message = on_message
client.on_disconnect = on_disconnect


client.loop_forever()
