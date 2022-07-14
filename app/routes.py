from threading import Lock
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
from app import app, socketio, db
from app.models import Event
from datetime import datetime


thread = None
thread_lock = Lock()
isTimerStarted = False

def background_thread():
    TIMER_INTERVAL = 0.5
    value = 0
    while True:
        socketio.sleep(TIMER_INTERVAL)
        socketio.emit(
            'my_response',
            {'data': 'Server timer event', 'timer': value}
        )
        value = value + TIMER_INTERVAL if isTimerStarted else 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle', methods=['POST'])
def stop():
    event = Event()
    event.from_dict({
        'timestamp': datetime.strptime(request.form.get('timestamp'), "%Y-%m-%dT%H:%M:%S.%fZ"),
        'value': request.form.get('value'),
        'event': request.form.get('event')
    })
    db.session.add(event)
    db.session.commit()

    global isTimerStarted
    isTimerStarted = not isTimerStarted
    
    return jsonify()

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