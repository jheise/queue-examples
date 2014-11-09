#!/usr/bin/env python
import pika
import msgpack

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='hack_fortress',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = ["hack"]

for binding_key in binding_keys:
    channel.queue_bind(exchange='hack_fortress',
                       queue=queue_name,
                       routing_key=binding_key)

print ' [*] Waiting for events. To exit press CTRL+C'

def callback(ch, method, properties, body):
    msg = msgpack.unpackb(body)
    print " [x] %r:%r" % (method.routing_key, msg)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
