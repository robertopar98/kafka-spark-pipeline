from confluent_kafka import Producer
import json
import time
from pydantic import BaseModel
import os

# Example Pydantic message schema
class TransactionMessage(BaseModel):
    id: int
    user: str
    amount: float
    timestamp: float

def delivery_report(err, msg):
    """Callback for message delivery reports"""
    if err is not None:
        print(f"❌ Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"✅ Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def create_producer():
    conf = {
        "bootstrap.servers": os.getenv("KAFKA_BROKER", "kafka:9092"),
    }
    return Producer(conf)

def run_producer(topic="customer_events"):
    producer = create_producer()

    for i in range(5):
        message = TransactionMessage(
            id=i,
            user=f"user_{i}",
            amount=round(100.0 + i * 10, 2),
            timestamp=time.time(),
        )

        producer.produce(
            topic=topic,
            key=str(message.id),
            value=json.dumps(message.dict()).encode("utf-8"),
            callback=delivery_report,
        )

        producer.flush()
        time.sleep(1)

if __name__ == "__main__":
    run_producer()
