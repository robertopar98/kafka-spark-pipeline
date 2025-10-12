from confluent_kafka import Consumer
import json
import os


def create_consumer(topic="transactions", group_id="debug-consumer"):
    conf = {
        "bootstrap.servers": os.getenv("KAFKA_BROKER", "kafka:9092"),
        "group.id": group_id,
        "auto.offset.reset": "earliest"
    }

    consumer = Consumer(conf)
    consumer.subscribe([topic])
    return consumer


def run_consumer():
    consumer = create_consumer()

    print("🟢 Listening for messages... (Ctrl+C to stop)")

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"⚠️ Consumer error: {msg.error()}")
                continue

            value = msg.value().decode("utf-8")
            print(f"📩 Received: {json.loads(value)}")

    except KeyboardInterrupt:
        print("🛑 Stopping consumer...")
    finally:
        consumer.close()


if __name__ == "__main__":
    run_consumer()
