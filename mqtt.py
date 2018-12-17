
import paho.mqtt.client as mqtt
import os, urlparse
import serial

#ser = serial.Serial('com15',9600)
# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    #ser.write(str(msg.payload))
def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)
try:
    mqttc = mqtt.Client()
    # Assign event callbacks
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe

    # Uncomment to enable debug messages
    #mqttc.on_log = on_log

    # Parse CLOUDMQTT_URL (or fallback to localhost)
    #url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://localhost:1883')
    #url = urlparse.urlparse(url_str)
    #topic = url.path[1:] or 'test'

    # Connect
    mqttc.username_pw_set("username", "password")
    mqttc.connect('server', port, 60)

    # Start subscribe, with QoS level 0
    a = mqttc.subscribe("/frommothership", 0)
    b = mqttc.subscribe("lat",0);
    b = mqttc.subscribe("project",0);

    # Publish a message
    #mqttc.publish("/frommothership","addresses" )

    # Continue the network loop, exit when an error occurs
    rc = 0
    while True :
        #mqttc.publish("/frommothership", "my message")
        rc = mqttc.loop()
    print("rc: " + str(rc))

except:
    exit
    #ser.close()
