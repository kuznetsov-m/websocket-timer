from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import eventlet
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
async_mode = 'eventlet'
socketio = SocketIO(app, transports=['websocket', 'polling'], async_mode=async_mode, cors_allowed_origins="*", \
    # logger=True, engineio_logger=True
)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
