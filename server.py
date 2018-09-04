from flask import Flask, request, jsonify, render_template
from flask_restful import Api
from flask_socketio import SocketIO, send

app = Flask("myapp")
api = Api(app)
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def Index():
    return render_template('index.html')


@app.route('/data', methods=['GET'])
def GetData():
    data = [
        {'id': 1, 'name': 'Juan'},
        {'id': 2, 'name': 'Mañe'},
        {'id': 3, 'name': 'Rober'},
        {'id': 4, 'name': 'Mari'},
        {'id': 5, 'name': 'Zuleima'}
    ]
    return jsonify(data)


@socketio.on('info')
def HandleMessage(data):
    print(data)
    socketio.emit('info', f"Hello from Python + Flask, {data['name']}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
    socketio.run(app)
