from datetime import datetime, timezone
from flightdex2_app.models._db import db
from flightdex2_app.models._datatypes import UTCDateTime, Encrypted, Password
from flightdex2_app.models._tables import *


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(UTCDateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))
    date_updated = db.Column(UTCDateTime(timezone=True))

    name = db.Column(db.String(256), nullable=False)
    number = db.Column(Encrypted, nullable=False)
    institution = db.Column(db.String(128))
    expiration = db.Column(Encrypted, nullable=False)
    security = db.Column(Password, nullable=False)
    nickname = db.Column(db.String(128))

    address = db.relationship('Address', uselist=False, backref='card', lazy='joined')

    cards = db.relationship('User', secondary=user_cards, backref=db.backref('cards', lazy=True))
