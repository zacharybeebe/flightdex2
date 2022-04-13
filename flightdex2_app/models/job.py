import json
from datetime import datetime, timezone
from flightdex2_app.models._db import db
from flightdex2_app.models._datatypes import UTCDateTime
from flightdex2_app.models._tables import *

# CREATE CUSTOM MODEL HERE
# IF CREATING MORE MODELS IN SEPARATE .PY FILES GO TO MODELS.__INIT__.PY AND IMPORT THE NEW MODEL
# THE MAIN __INIT__.PY FOR THE APP WILL IMPORT * FROM MODELS.__INIT__.PY


class Job(db.Model):
	proposal_attrs = ['id', 'project_price', 'hourly_price']

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(UTCDateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))

	type = db.Column(db.String(128), nullable=False)
	sub_type = db.Column(db.String(128), nullable=False)
	other_sub_type = db.Column(db.String(256))
	status = db.Column(db.String(16), nullable=False)

	project_price = db.Column(db.Float)
	hourly_price = db.Column(db.Float)

	date_target = db.Column(db.DateTime(timezone=True), nullable=False)
	time = db.Column(db.String(8), nullable=False)
	state = db.Column(db.String(64), nullable=False)
	metro = db.Column(db.String(128), nullable=False)
	title = db.Column(db.String(256))
	description = db.Column(db.String(8192))

	has_deliverables = db.Column(db.Boolean, nullable=False, default=False)

	client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	pro_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=-1)

	address = db.relationship('Address', uselist=False, backref='job', lazy=True)

	jobs = db.relationship('User', secondary=user_jobs, backref=db.backref('jobs', lazy=True))

	# Relationship Tables References
	# attachments -> backrefs to job_attachments table
	# deliverables -> backrefs to job_deliverables table
	# proposals -> backrefs to job_proposals table

	def get_proposal_attrs(self):
		return json.dumps({attr: self.__dict__[attr] for attr in self.proposal_attrs})

