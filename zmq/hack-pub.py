#!/usr/bin/env python
import msgpack
import time
import zmq
from datetime import datetime


ctx = zmq.Context.instance()
publisher = ctx.socket(zmq.PUB)
publisher.bind("tcp://*:6000")

for x in range(30):
    body = {"time":str(datetime.now()), "team":"red", "action":"slap"}
    msg = "HACK PURCHASE {0}".format(msgpack.packb(body))
    print msg
    #msg = msgpack.packb(msg)
    #print msg
    try:
        publisher.send(msg)
    except zmq.ZMQError as e:
        if e.errno == zmq.ETERM:
            break
        else:
            raise
    time.sleep(1)

publisher.send("HACK END")

ctx.term()
print "hack pub finished"
