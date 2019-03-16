import explorerhat
from flask import Flask
from flask import jsonify
app = Flask(__name__)
class DataStore():
    speed = 0
    mod = 5
    direction = 'forwards'
data = DataStore()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/car/forward')
def forward():
    if data.speed+data.mod<=100:
        data.speed = data.speed + data.mod
    if data.speed>=0:
        data.direction = 'forwards'
        explorerhat.motor.forwards(data.speed)
    else:
        data.direction = 'backwards'
        explorerhat.motor.backwards(data.speed*-1)
    jsonData = jsonify({'direction': data.direction, 'speed': data.speed})
    return jsonData
@app.route('/car/backward') 
def backward():
     if data.speed+data.mod<=-100:
         data.speed = data.speed - data.mod
     if data.speed>=0:
         data.direction = 'forwards'
         explorerhat.motor.forwards(data.speed)
     else:
         data.direction = 'backwards'
         explorerhat.motor.backwards(data.speed*-1)
     jsonData = jsonify({'direction': data.direction, 'speed': data.speed})
     return jsonData

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
    #app.run(port=80)
