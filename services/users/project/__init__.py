
from flask import Flask, jsonify


# instantiate the app
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
