from flightdex2_app.models._db import db

conversation_messages = db.Table(
    'conversation_messages',
    db.Column('conversation_id', db.Integer, db.ForeignKey('conversation.id'), primary_key=True),
    db.Column('message_id', db.Integer, db.ForeignKey('message.id'), primary_key=True)
)


job_attachments = db.Table(
    'job_attachments',
    db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True),
    db.Column('attachment_id', db.Integer, db.ForeignKey('attachment.id'), primary_key=True)
)


job_deliverables = db.Table(
    'job_deliverables',
    db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True),
    db.Column('deliverable_id', db.Integer, db.ForeignKey('deliverable.id'), primary_key=True)
)


job_proposals = db.Table(
    'job_proposals',
    db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True),
    db.Column('proposal_id', db.Integer, db.ForeignKey('proposal.id'), primary_key=True)
)


user_banks = db.Table(
    'user_banks',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('bank_id', db.Integer, db.ForeignKey('bank.id'), primary_key=True)
)

user_cards = db.Table(
    'user_cards',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('card_id', db.Integer, db.ForeignKey('card.id'), primary_key=True)
)


user_conversations = db.Table(
    'user_conversations',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('conversation_id', db.Integer, db.ForeignKey('conversation.id'), primary_key=True)
)


user_friends = db.Table(
    'user_friends',
    db.Column('userA_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('userB_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)


user_jobs = db.Table(
    'user_jobs',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True)
)


user_proposals = db.Table(
    'user_proposals',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('proposal_id', db.Integer, db.ForeignKey('proposal.id'), primary_key=True)
)

