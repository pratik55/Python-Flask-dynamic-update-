
from flask import Flask, jsonify, render_template, request
import webbrowser
import time

app = Flask(__name__)

@app.route('/_stuff', methods = ['GET'])
def stuff():
        
    return jsonify(result=time.time())


@app.route('/')
def index():
   
    return render_template('dy1.html')

    
if __name__ == '__main__':
    
    app.run()
