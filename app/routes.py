from threading import Lock
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
from app import app, socketio, db
from app.models import Event
from datetime import datetime


thread = None
thread_lock = Lock()
is_timer_started = False

def background_thread():
    TIMER_INTERVAL = 0.5
    value = 0
    while True:
        socketio.sleep(TIMER_INTERVAL)
        socketio.emit(
            'timer_event',
            {'data': 'Server timer event', 'value': value, 'is_started': is_timer_started}
        )
        value = value + TIMER_INTERVAL if is_timer_started else 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle', methods=['POST'])
def toggle():
    event = Event()
    event.from_dict({
        'timestamp': datetime.strptime(request.form.get('timestamp'), "%Y-%m-%dT%H:%M:%S.%fZ"),
        'value': request.form.get('value'),
        'event': request.form.get('event')
    })
    db.session.add(event)
    db.session.commit()

    timer_events = {
        'start': True,
        'stop': False
    }

    global is_timer_started
    is_timer_started = timer_events.get(request.form.get('event').lower())

    data = {
        'timestamp': request.form.get('timestamp'),
        'value': request.form.get('value'),
        'event': request.form.get('event'),
    }

    socketio.emit('timer_toggle_event', data)
    
    return data

@socketio.event
def my_ping():
    emit('my_pong')

@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    # global is_timer_started
    # emit('my_response', {'data': 'Connected', 'is_timer_started': is_timer_started})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)