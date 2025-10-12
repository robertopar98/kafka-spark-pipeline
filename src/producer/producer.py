import os
import json
import time
import random
from kafka import KafkaProducer
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=".env.dev")

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "test-topic")

def create_producer():
    """Initialize Kafka producer."""
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    return producer

def send_random_messages(producer, topic=KAFKA_TOPIC):
    """Send random test messages to Kafka."""
    for i in range(10):
        message = {"event_id": i, "value": random.random(), "timestamp": time.time()}
        producer.send(topic, value=message)
        print(f"Sent: {message}")
        time.sleep(1)

if __name__ == "__main__":
    producer = create_producer()
    send_random_messages(producer)
    producer.flush()
