import os
import paho.mqtt.client as mqtt
from pymongo import MongoClient

# Load credentials from environment variables
USERNAME = os.getenv("MQTT_USER")
PASSWORD = os.getenv("MQTT_PASSWORD")

# MQTT Configuration
BROKER = "localhost"
PORT = 1883
TOPIC = "#"

# MongoDB Configuration
MONGO_CLIENT = MongoClient("mongodb://localhost:27017/")
DB = MONGO_CLIENT["mqtt_data"]
COLLECTION = DB["messages"]

def on_message(client, userdata, msg):
    message = {"topic": msg.topic, "payload": msg.payload.decode()}
    COLLECTION.insert_one(message)
    print(f"Stored in MongoDB: {message}")

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)  # Use env variables
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)
client.on_message = on_message

print("📡 Listening for MQTT messages and storing them in MongoDB...")
client.loop_forever()
