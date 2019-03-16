from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/car/forward')
def forward():
    print('forward')
    data = jsonify({'car': 'forwards'})
    return data

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
    #app.run(port=80)
