from kafka import KafkaConsumer
import json

def create_consumer(topic="test-topic"):
    """Initialize a Kafka consumer."""
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers="kafka:9092",
        auto_offset_reset="earliest",     # read messages from the beginning
        enable_auto_commit=True,          # automatically commit offsets
        group_id="my-consumer-group",     # consumers with same group_id share the load
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )
    return consumer

def consume_messages(consumer):
    """Continuously consume messages."""
    print("Listening for messages... (Ctrl+C to stop)\n")

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
