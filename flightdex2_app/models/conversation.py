from datetime import datetime, timezone
from flightdex2_app.models._db import db
from flightdex2_app.models._datatypes import UTCDateTime
from flightdex2_app.models._tables import *


class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(UTCDateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))

    subject = db.Column(db.String(256), default='No Subject')

    userA_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    userB_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    conversations = db.relationship('User', secondary=user_conversations, backref=db.backref('conversations', lazy=True))

    # Relationship Tables References
    # messages -> backrefs to conversation_messages table