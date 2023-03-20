from confluent_kafka import Consumer, KafkaException, KafkaError
import socket, json, time, traceback
from controller import consume_sql_action

conf = {'bootstrap.servers': "distributedfinal-broker-1:29092",
        'group.id': socket.gethostname(),
        'auto.offset.reset': 'smallest'}
consumer = Consumer(conf)
running = True
connected = False

def consume_loop(topics):
    try:
        # try connecting after delay to avoid race condition
        wait_connect(topics)
        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: 
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    print('%% %s [%d] reached end at offset %d\n' % (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                # message consumed, convert it to a dict
                data = msg.value().decode('utf-8')
                data = json.loads(data)
                
                # update system logs
                print("Message converted and read as: " + str(data))
                
                # perform action
                try:
                    consume_sql_action(action=data['action'], table=data['table'], data=data['data'])
                except Exception:
                    traceback.print_exc()
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

def wait_connect(topics):
    print("Waiting before connecting...")
    time.sleep(15)
    consumer.subscribe(topics)
    print("Connected to topic(s): " + str(topics))

def shutdown():
    running = False
