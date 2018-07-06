
from flask import Flask, jsonify, render_template, request
import webbrowser
import time

app = Flask(__name__)

@app.route('/_stuff', methods = ['GET'])
def stuff():
    lat = time.time()/77500000
    longi = time.time()/20800000
    
    return jsonify(lat=lat,longi=longi)
    

@app.route('/')
def index():
   
    return render_template('finalguess.html')

    
if __name__ == '__main__':
    
    app.run()
