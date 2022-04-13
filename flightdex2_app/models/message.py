from datetime import datetime, timezone
from flightdex2_app.models._db import db
from flightdex2_app.models._datatypes import UTCDateTime
from flightdex2_app.models._tables import *


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_sent = db.Column(UTCDateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))
    date_read = db.Column(UTCDateTime(timezone=True))

    #subject = db.Column(db.String(256), default='No Subject')
    message = db.Column(db.String(32768), nullable=False)

    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    messages = db.relationship('Conversation', secondary=conversation_messages, backref=db.backref('messages', lazy=True))
