import explorerhat
from flask import Flask
from flask import jsonify
from flask import render_template
app = Flask(__name__)
class DataStore():
    speed1 = 60
    speed2 = 60
    mod = 5
data = DataStore()

@app.route('/')
def home():
    return render_template('car.html')

@app.route('/car/forward')
def forward():
    speedN = max(data.speed1, data.speed2, 60)
    data.speed1 = speedN + data.mod
    data.speed2 = speedN + data.mod
    explorerhat.motor.one.speed(data.speed1)
    explorerhat.motor.two.speed(data.speed2)
    jsonData = jsonify({'speed1': data.speed1, 'speed2': data.speed2})
    return jsonData
@app.route('/car/backward') 
def backward():
    speedN = min(data.speed1, data.speed2, -60)
    data.speed1 = speedN - data.mod
    data.speed2 = speedN - data.mod
    explorerhat.motor.one.speed(data.speed1)
    explorerhat.motor.two.speed(data.speed2)
    jsonData = jsonify({'speed1': data.speed1, 'speed2': data.speed2})
    return jsonData
@app.route('/car/left') 
def left():
    data.speed1 = 100
    data.speed2 = 0
    explorerhat.motor.one.speed(data.speed1)
    explorerhat.motor.two.speed(data.speed2)
    jsonData = jsonify({'speed1': data.speed1, 'speed2': data.speed2})
    return jsonData
@app.route('/car/right') 
def right():
    data.speed1 = 0
    data.speed2 = 100
    explorerhat.motor.one.speed(data.speed1)
    explorerhat.motor.two.speed(data.speed2)
    jsonData = jsonify({'speed1': data.speed1, 'speed2': data.speed2})
    return jsonData

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
    #app.run(port=80)
