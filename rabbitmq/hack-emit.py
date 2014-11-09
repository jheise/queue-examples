#!/usr/bin/env python
import pika
import msgpack
import datetime
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='hack_fortress',
                         type='topic')

routing_key = 'hack'
for x in range(30):
    message = { "time":str(datetime.datetime.now()), "team":"red", "event":"slap" }
    msg = msgpack.packb(message)
    channel.basic_publish(exchange='hack_fortress',
                          routing_key=routing_key,
                          body=msg)
    print " [x] Sent %r:%r" % (routing_key, message)
    time.sleep(1)
connection.close()

