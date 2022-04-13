from datetime import datetime, timezone
from flightdex2_app.models._db import db
from flightdex2_app.models._datatypes import Blob, UTCDateTime
from flightdex2_app.models._tables import *


class Deliverable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_uploaded = db.Column(UTCDateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))
    filename = db.Column(db.String(256))
    content = db.Column(Blob)

    deliverables = db.relationship('Job', secondary=job_deliverables, backref=db.backref('deliverables', lazy=True))
