import os
import json
from kafka import KafkaConsumer
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=".env.dev")

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "test-topic")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "my-consumer-group")
KAFKA_AUTO_OFFSET_RESET = os.getenv("KAFKA_AUTO_OFFSET_RESET", "earliest")

def create_consumer():
    """Initialize Kafka consumer."""
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        auto_offset_reset=KAFKA_AUTO_OFFSET_RESET,
        enable_auto_commit=True,
        group_id=KAFKA_GROUP_ID,
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )
    return consumer

def consume_messages(consumer):
    """Continuously consume messages."""
    print(f"Listening for messages on topic '{KAFKA_TOPIC}'...\n")
    try:
        for message in consumer:
            print(f"Received message: {message.value}")
    except KeyboardInterrupt:
        print("\nStopped consuming.")
    finally:
        consumer.close()

if __name__ == "__main__":
    consumer = create_consumer()
    consume_messages(consumer)
