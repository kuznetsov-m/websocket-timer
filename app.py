from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
socketio = SocketIO(app)
thread = None
thread_lock = Lock()

def background_thread():
    TIMER_INTERVAL = 0.5
    value = 0
    while True:
        socketio.sleep(TIMER_INTERVAL)
        value += TIMER_INTERVAL
        socketio.emit(
            'my_response',
            {'data': 'Server timer event', 'timer': value}
        )

@app.route('/')
def index():
    return render_template('index.html')

@socketio.event
def my_ping():
    emit('my_pong')

@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app)