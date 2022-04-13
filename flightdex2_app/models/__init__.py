# IMPORT ALL MODELS AND DB TO HERE AND THEN THE MAIN __INIT__.PY WILL
# IMPORT * FROM HERE


from flightdex2_app.models._db import db
from flightdex2_app.models.address import Address
from flightdex2_app.models.attachment import Attachment
from flightdex2_app.models.bank import Bank
from flightdex2_app.models.card import Card
from flightdex2_app.models.conversation import Conversation
from flightdex2_app.models.deliverable import Deliverable
from flightdex2_app.models.job import Job
from flightdex2_app.models.message import Message
from flightdex2_app.models.proposal import Proposal
from flightdex2_app.models.user import User




