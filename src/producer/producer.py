from google.cloud import pubsub_v1
import json
import time
import random

project_id = "gcp-retail-streaming-pipeline"
topic_id = "retail-events-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)


def generate_event():
    event = {
        "event_id": f"EVT{random.randint(1000,9999)}",
        "customer_id": f"C{random.randint(100,999)}",
        "product_id": f"P{random.randint(100,999)}",
        "event_type": random.choice(["view", "add_to_cart", "purchase"]),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(5, 100), 2),
        "event_time": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return event


while True:
    event = generate_event()
    data = json.dumps(event).encode("utf-8")

    future = publisher.publish(topic_path, data)
    message_id = future.result()
    print(f"Published message_id={message_id}: {event}")

    time.sleep(2)