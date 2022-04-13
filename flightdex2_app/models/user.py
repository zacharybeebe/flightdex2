from datetime import datetime, timezone
from flightdex2_app.models._db import db
from flightdex2_app.models._datatypes import Password, UTCDateTime
from flightdex2_app.models._tables import *

# CREATE CUSTOM MODEL HERE
# IF CREATING MORE MODELS IN SEPARATE .PY FILES GO TO MODELS.__INIT__.PY AND IMPORT THE NEW MODEL
# THE MAIN __INIT__.PY FOR THE APP WILL IMPORT * FROM MODELS.__INIT__.PY


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(UTCDateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))
	last_login = db.Column(UTCDateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))

	type = db.Column(db.String(32), nullable=False)
	f_name = db.Column(db.String(128), nullable=False)
	l_name = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(128), nullable=False, unique=True)
	phone = db.Column(db.String(16), nullable=False)
	company = db.Column(db.String(128))
	state = db.Column(db.String(64), nullable=False)
	metro = db.Column(db.String(128), nullable=False)

	username = db.Column(db.String(128), nullable=False, unique=True)
	password = db.Column(Password, nullable=False)

	is_online = db.Column(db.Boolean, default=False)

	address = db.relationship('Address', uselist=False, backref='user', lazy=True)

	friends = db.relationship('User', secondary=user_friends, primaryjoin=id == user_friends.c.userA_id, secondaryjoin=id == user_friends.c.userB_id)

	# Relationship Tables References
	# banks -> backrefs to user_banks table
	# cards -> backrefs to user_cards table
	# conversations -> backrefs to user_conversations table
	# friends -> backrefs to user_friends table
	# jobs -> backrefs to user_jobs table
	# proposals -> backrefs to user_proposals table

	def show_all(self):
		print('Address:')
		print(f'\t{self.address.street=}')
		print(f'\t{self.address.apt=}')
		print(f'\t{self.address.city=}')
		print(f'\t{self.address.state=}')
		print(f'\t{self.address.zip_code=}\n')

		print('Banks:')
		for i, bank in enumerate(self.banks, 1):
			print(f'\tBank {i}:')
			print(f'\t\t{bank.routing=}')
			print(f'\t\t{bank.account=}')
			print(f'\t\t{bank.institution=}')
		print()

		print('Cards:')
		for i, card in enumerate(self.cards, 1):
			print(f'\tCard {i}:')
			print(f'\t\t{card.name=}')
			print(f'\t\t{card.number=}')
			print(f'\t\t{card.expiration=}')
			print(f'\t\t{card.security=}')
			print(f'\t\t{card.institution=}')
			print(f'\t\t{card.nickname=}')
			print('\t\tCard Address:')
			print(f'\t\t\t{card.address.street=}')
			print(f'\t\t\t{card.address.apt=}')
			print(f'\t\t\t{card.address.city=}')
			print(f'\t\t\t{card.address.state=}')
			print(f'\t\t\t{card.address.zip_code=}\n')
		print()

		print('Conversations:')
		for i, conv in enumerate(self.conversations, 1):
			print(f'\tConversation {i}:')
			print(f'\t\t{conv.subject=}')
			for message in conv.messages:
				if message.sender_id == self.id:
					print(f'\t\t\tSent: {message.message}')
				else:
					print(f'\t\t\tReply: {message.message}')
		print()

		print('Jobs:')
		for i, job in enumerate(self.jobs, 1):
			print(f'Job {i}:')
			print(f'\t\t{job.type=}')
			print(f'\t\t{job.sub_type=}')
			print(f'\t\t{job.status=}')
			print(f'\t\t{job.project_price=}')
			print(f'\t\t{job.hourly_price=}')
			print(f'\t\t{job.date_target=}')
			print(f'\t\t{job.time=}')
			print(f'\t\t{job.state=}')
			print(f'\t\t{job.metro=}')
			print(f'\t\t{job.title=}')
			print(f'\t\t{job.description=}')
			print('\t\tJob Address:')
			print(f'\t\t\t{job.address.street=}')
			print(f'\t\t\t{job.address.apt=}')
			print(f'\t\t\t{job.address.city=}')
			print(f'\t\t\t{job.address.state=}')
			print(f'\t\t\t{job.address.zip_code=}\n')
		print()

		print('Proposals:')
		for i, prop in enumerate(self.proposals, 1):
			print(f'Proposal {i}:')
			print(f'\t\t{prop.job_id=}')
			print(f'\t\t{prop.bid=}')
			print(f'\t\t{prop.description=}')
























