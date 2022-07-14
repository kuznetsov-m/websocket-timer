from datetime import datetime
from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow, unique=True)
    value = db.Column(db.String(120))
    event = db.Column(db.String(120))

    def __repr__(self):
        return f'<Event {self.timestamp} {self.value} {self.event}>'

    def from_dict(self, data, new_user=False):
        for field in ['timestamp', 'value', 'event']:
            if field in data:
                setattr(self, field, data[field])