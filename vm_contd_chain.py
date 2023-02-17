import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

load_ping = 0
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("linuslei/ping")
    client.message_callback_add("linuslei/ping", on_message_ping)

def on_message_ping(client, userdata, msg):

    print("Custom Callback" + str(msg.payload.decode("utf-8")))
    client.publish("linuslei/pong", int(msg.payload.decode())+1)
    print("Pong")
    time.sleep(4)

if __name__ == '__main__':
    #get IP address
    ip_address='172.20.10.10' 

  
    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python. For example:
    
    `client.connect("eclipse.usc.edu", 11000, 60)` 
    
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    client.connect(host="172.20.10.10", port=1883, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""

    #replace user with your USC username in all subscriptions
    client.loop_forever()