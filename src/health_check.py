import psycopg2
from kafka import KafkaProducer
import socket

# Kafka check
try:
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    producer.send('health-test', b'ping')
    producer.flush()
    print("Kafka OK")
except Exception as e:
    print("Kafka ERROR:", e)

# Postgres check
try:
    conn = psycopg2.connect(
        host='postgres',
        dbname='pipeline_db',
        user='admin',
        password='admin',
        port=5432
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    if cur.fetchone() == (1,):
        print("Postgres OK")
    conn.close()
except Exception as e:
    print("Postgres ERROR:", e)


# Spark check (ping master)
try:
    sock = socket.create_connection(("spark", 7077), timeout=5)
    print("Spark connection OK")
except Exception as e:
    print("Spark ERROR:", e)