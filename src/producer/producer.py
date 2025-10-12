from kafka import KafkaProducer
import json
import time
import random

def create_producer():
    """Initialize a Kafka producer."""
    producer = KafkaProducer(
        bootstrap_servers="kafka:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")  # convert dict → JSON → bytes
    )
    return producer

def send_messages(producer, topic="test-topic"):
    """Send sample messages to Kafka."""
    print(f"Producing messages to topic '{topic}'... (Ctrl+C to stop)")

    try:
        while True:
            message = {
                "event_id": random.randint(1, 1000),
                "value": random.random(),
                "timestamp": time.time(),
            }
            producer.send(topic, message)
            print("Sent:", message)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Stopped producing.")
    finally:
        producer.close()

if __name__ == "__main__":
    producer = create_producer()
    send_messages(producer)
