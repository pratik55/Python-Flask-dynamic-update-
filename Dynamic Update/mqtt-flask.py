from flask import Flask, jsonify, render_template, request
from flask_mqtt import Mqtt
import time



lat = 19.22
longi = 72.86

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'Your server'
app.config['MQTT_BROKER_PORT'] = Your port
app.config['MQTT_USERNAME'] = 'Your Username'
app.config['MQTT_PASSWORD'] = 'Your Password'
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('lat')
    mqtt.subscribe('longi')



@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    #data = dict(
     #   topic=message.topic,
      #  payload=message.payload.decode()
    #)
    global lat
    global longi
    topic = message.topic
    if topic == 'lat':
        lat = float(message.payload.decode())
        print(lat)
    if topic == 'longi':
        longi = float(message.payload.decode())
        print(longi)


@app.route('/_stuff', methods = ['GET'])
def stuff():
    global lat
    global longi

    
    return jsonify(lat=lat,longi=longi)



@app.route('/')
def index():
    return render_template('finalguess.html')

if __name__ == '__main__':
    
    app.run()
