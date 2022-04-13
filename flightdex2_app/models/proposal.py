import json
from datetime import datetime, timezone
from flightdex2_app.models._db import db
from flightdex2_app.models._datatypes import UTCDateTime
from flightdex2_app.models._tables import *

# CREATE CUSTOM MODEL HERE
# IF CREATING MORE MODELS IN SEPARATE .PY FILES GO TO MODELS.__INIT__.PY AND IMPORT THE NEW MODEL
# THE MAIN __INIT__.PY FOR THE APP WILL IMPORT * FROM MODELS.__INIT__.PY


class Proposal(db.Model):
    proposal_attrs = ['id', 'bid', 'description']
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(UTCDateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))
    date_updated = db.Column(UTCDateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))

    bid = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(4096), nullable=False)
    pro_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)

    user_proposals = db.relationship('User', secondary=user_proposals, backref=db.backref('proposals', lazy=True))
    job_proposals = db.relationship('Job', secondary=job_proposals, backref=db.backref('proposals', lazy=True))

    def get_proposal_attrs(self):
        return json.dumps({attr: self.__dict__[attr] for attr in self.proposal_attrs})