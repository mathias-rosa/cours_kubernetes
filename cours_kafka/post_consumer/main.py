from kafka import KafkaConsumer
import json

# Configure the Kafka consumer
consumer = KafkaConsumer(
    'posts',
    bootstrap_servers=['10.244.3.9:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='post-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Consume messages
print("Starting consumer...")
for message in consumer:
    print(f"Topic: {message.topic}")
    print(f"Partition: {message.partition}")
    print(f"Offset: {message.offset}")
    print(f"Key: {message.key}")
    print(f"Value: {message.value}")
    print("-" * 50)