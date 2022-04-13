from datetime import datetime, timezone
from flightdex2_app.models._db import db
from flightdex2_app.models._datatypes import Password, UTCDateTime
from flightdex2_app.models._tables import *

# CREATE CUSTOM MODEL HERE
# IF CREATING MORE MODELS IN SEPARATE .PY FILES GO TO MODELS.__INIT__.PY AND IMPORT THE NEW MODEL
# THE MAIN __INIT__.PY FOR THE APP WILL IMPORT * FROM MODELS.__INIT__.PY


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(256), nullable=False)
    apt = db.Column(db.String(256))
    city = db.Column(db.String(256), nullable=False)
    state = db.Column(db.String(256), nullable=False)
    zip_code = db.Column(db.String(256), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))
