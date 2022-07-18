from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit #, disconnect

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
import eventlet

async_mode = 'eventlet'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, transports=['websocket', 'polling'], async_mode=async_mode, cors_allowed_origins="*", logger=True, engineio_logger=True)


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.event
def my_ping():
    emit('my_pong')


@socketio.event
def connect():
    print(f'[SERVER]: Client connnected {request.sid}')
    emit('my_response', {'data': 'Connected'})


@socketio.on('disconnect')
def test_disconnect():
    print(f'[SERVER]: Client disconnected {request.sid}')


if __name__ == '__main__':
    
    socketio.run(app)