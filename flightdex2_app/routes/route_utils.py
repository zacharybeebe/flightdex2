from datetime import date
from hashlib import sha256


def check_login(db, User, username_email, password):
    if username_email == '':
        return False, 'Please Enter a Username or Email', None
    else:
        user = get_model_by_field(db, User, 'username', username_email)
        if not user:
            user = get_model_by_field(db, User, 'email', username_email)
            if not user:
                return False, 'Incorrect Username or Email', None

        if user.password != sha256(password.encode('utf-8')).hexdigest():
            return False, 'Incorrect Password', None
        else:
            return True, None, user


def check_session(username, session):
    try:
        if 'user' in session:
            if username == session['user']:
                return True
            else:
                return False
        else:
            return False
    except KeyError:
        return False


def disengage_user(db, User, username, session):
    user = get_model_by_field(db, User, 'username', username)
    user.online = False
    session.pop('user', None)
    session.pop('date', None)
    session.pop('search', None)
    db.session.commit()


def get_model_by_field(db, model, field, value):
    return db.session.query(model).filter_by(**{field: value}).first()


def get_model_by_fields(db, model, **filters):
    return db.session.query(model).filter_by(**filters).first()


def initialize_user(db, user, session):
    user.is_online = True

    session['user'] = user.username
    session['date'] = [date.today().year, date.today().month]
    session['search'] = {
        'state': user.state,
        'metro': user.metro,
        'type': 'all',
        'price': 'all',
        'distance': 50
    }
    session.permanent = True
    db.session.commit()





