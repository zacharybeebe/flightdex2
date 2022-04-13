from datetime import timedelta
from flask import Flask
# from flask_login import ()
# from flask_mail import ()
# from flask_wft import ()
# from flask_debugtoolbar import ()
from flightdex2_app.config.app_config import *
from flightdex2_app.config.constants import *
from flightdex2_app.models import *


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
# app.config[''] = ''
# app.config[''] = ''
# app.config[''] = ''
app.permanent_session_lifetime = timedelta(seconds=360)


with app.app_context():
	db.init_app(app)

	REDO_DATABASE = False
	if REDO_DATABASE:
		from flightdex2_app.fake_data.fake_setup import generate_fake_data
		db.drop_all()
		db.create_all()
		generate_fake_data(db)


from flightdex2_app.routes import public
from flightdex2_app.routes import private
