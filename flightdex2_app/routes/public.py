from flask import render_template, redirect, url_for, request, session, flash, make_response, jsonify
from flightdex2_app import *
from flightdex2_app.routes.route_utils import check_login, check_session, disengage_user, get_model_by_field, initialize_user


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def index():
    return render_template('public/index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('public/about.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('public/contact.html')


@app.route('/info', methods=['GET'])
def info():
    return render_template('public/info.html')


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        print(request.form)
    return render_template('public/create_account.html', us_states=US_STATES, metros=METROS)


@app.route('/login', methods=['GET', 'POST'])
def login():
    flash = None
    username_email = ''
    if request.method == 'POST':
        username_email = request.form['username_email']
        proceed, flash, user = check_login(db, User, username_email, request.form['password'])
        if proceed:
            initialize_user(db, user, session)
            app.logger.info(f'{user.username} has logged in successfully')
            return redirect(url_for('dashboard', username=user.username))
        else:
            if flash == 'Incorrect Username or Email':
                return render_template('public/login.html', flash=flash, username='')
            else:
                return render_template('public/login.html', flash=flash, username=username_email)
    else:
        if 'user' in session:
            return redirect(url_for('dashboard', username=session['user']))
        else:
            return render_template('public/login.html', flash=flash, username=username_email)


@app.route('/<username>/logout')
def logout(username):
    disengage_user(db, User, username, session)
    app.logger.info(f'{username} has logged out successfully')
    return redirect(url_for('index'))


# Asynchronous Post Routes with JS Fetch API
@app.route('/check_database_<field>', methods=['POST'])
def check_database(field):
    post = request.get_json()
    print(post)
    valid = User.query.filter_by(**{field: post}).first() is None  # or []
    if valid:
        message = f'{field.capitalize()}: "{post}" is a valid {field}'
    else:
        message = f'{field.capitalize()}: "{post}" has already been taken'

    resp = make_response(jsonify({'message': message, 'valid': valid}, 200))
    return resp

