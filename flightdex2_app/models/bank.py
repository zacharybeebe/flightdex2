from datetime import datetime, timezone
from flightdex2_app.models._db import db
from flightdex2_app.models._datatypes import UTCDateTime, Encrypted
from flightdex2_app.models._tables import *


class Bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(UTCDateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))
    date_updated = db.Column(UTCDateTime(timezone=True))

    routing = db.Column(Encrypted, nullable=False)
    institution = db.Column(db.String(128))
    account = db.Column(Encrypted, nullable=False)

    banks = db.relationship('User', secondary=user_banks, backref=db.backref('banks', lazy=True))