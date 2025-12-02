from kafka import KafkaConsumer
import json
import argparse

def main(kafka_host=None):
    # Configure the Kafka consumer
    consumer = KafkaConsumer(
        'posts',
        bootstrap_servers=[kafka_host],
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

    # Main execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--kafka_host', type=str, required=False, default=None, help='The Kafka host address')
    args = parser.parse_args()

    main(
        kafka_host=args.kafka_host
    )