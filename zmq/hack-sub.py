#!/usr/bin/env python

import zmq
import msgpack

ctx = zmq.Context.instance()
subscriber = ctx.socket(zmq.SUB)
subscriber.connect("tcp://localhost:6000")
subscriber.setsockopt(zmq.SUBSCRIBE, b"HACK")

running = True
while running:
    try:
        msg = subscriber.recv_multipart()
        channel, subchannel, body = msg[0].split(" ",2)
        body = msgpack.unpackb(body)
        print  body
    except zmq.ZMQError as e:
        if e.errno == zmq.ETERM:
            break
        else:
            raise
    if body == "END":
        running = False

ctx.term()
print "hack sub finished"
