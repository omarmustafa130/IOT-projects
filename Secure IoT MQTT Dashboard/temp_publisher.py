import paho.mqtt.client as mqtt
import time
from dotenv import load_dotenv
import os
import random
load_dotenv()

LOCAL_BROKER = os.getenv("LOCAL_BROKER")
LOCAL_USERNAME = os.getenv("LOCAL_USERNAME")
LOCAL_PASSWORD = os.getenv("LOCAL_PASSWORD")
LOCAL_PORT = 1883

REMOTE_BROKER = os.getenv("REMOTE_BROKER")
REMOTE_USERNAME = os.getenv("REMOTE_USERNAME")
REMOTE_PASSWORD = os.getenv("REMOTE_PASSWD")
REMOTE_PORT = 1883
TOPIC = "/sensor/temperature"


def publish_temperature():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    client.username_pw_set(LOCAL_USERNAME, LOCAL_PASSWORD)
    client.connect(LOCAL_BROKER, LOCAL_PORT)

    while True:
        temp = round(random.uniform(20, 30), 2)
        print(f"Publishing Temperature: {temp}°C")
        client.publish(TOPIC, str(temp), qos=1, retain=True)
        time.sleep(3)

publish_temperature()
