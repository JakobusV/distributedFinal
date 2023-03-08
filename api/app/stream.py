from confluent_kafka import Producer
import socket, json

topic = "database"

conf = {
    'bootstrap.servers': "172.22.0.4:29092",
    'client.id': socket.gethostname()
}

def result(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

def send_json(topic: str, data: dict):
    data = json.dumps(data, sort_keys=True, indent=4)
    producer = Producer(conf)
    producer.poll(0)
    producer.produce(topic, data, callback=result)
    producer.flush()