from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

payment = {
    "user_id": "U789",
    "amount": 15000,
    "currency": "USD",
    "timestamp": int(time.time())
}

producer.send('test', value=payment)
producer.flush()
print("Sent:", payment)