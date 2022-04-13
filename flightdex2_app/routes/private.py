from datetime import datetime, timezone
from flask import render_template, redirect, url_for, request, session, flash, make_response, jsonify
from flightdex2_app import *
from flightdex2_app.routes.route_utils import check_session, get_model_by_field, get_model_by_fields


@app.route('/user/<username>/dashboard', methods=['GET'])
def dashboard(username):
    if check_session(username, session):
        user = get_model_by_field(db, User, 'username', username)
        # year, month = session['date']
        # notification_count = user.get_unread_notifications(user.received_notifications)
        # job_snapshot = user.get_month_snapshot(user)
        return render_template('private/dashboard.html', user=user)
    else:
        return redirect(url_for('login'))


@app.route('/user/<username>/jobs/<jobs_status>', methods=['GET'])
def jobs(username, jobs_status):
    if check_session(username, session):
        proposal_job_ids = None
        user = get_model_by_field(db, User, 'username', username)
        jobs = sorted([job for job in user.jobs if job.status == jobs_status], key=lambda x: x.date_target)
        if user.type == 'Drone Pro' and jobs_status == 'posted':
            jobs_status = 'interested'
            proposal_job_ids = [proposal.job_id for proposal in user.proposals]

        # year, month = session['date']
        # notification_count = user.get_unread_notifications(user.received_notifications)
        # job_snapshot = user.get_month_snapshot(user)
        return render_template('private/jobs.html', user=user, jobs=jobs, jobs_status=jobs_status, proposal_job_ids=proposal_job_ids)
    else:
        return redirect(url_for('login'))


@app.route('/user/<username>/job/<job_id>', methods=['GET'])
def job(username, job_id):
    if check_session(username, session):
        client = None
        proposal = None
        user = get_model_by_field(db, User, 'username', username)
        job = get_model_by_field(db, Job, 'id', int(job_id))
        if user.type == 'Drone Pro':
            client = get_model_by_field(db, User, 'id', job.client_id)
            proposal = get_model_by_fields(db, Proposal, pro_id=user.id, job_id=job.id)
            print(f'{proposal=}')


        # year, month = session['date']
        # notification_count = user.get_unread_notifications(user.received_notifications)
        # job_snapshot = user.get_month_snapshot(user)
        return render_template('private/job.html', user=user, job=job, client=client, proposal=proposal)
    else:
        return redirect(url_for('login'))


# Synchronous Post Routes with Redirect
@app.route('/submit_proposal', methods=['POST'])
def submit_proposal():
    pro = get_model_by_field(db, User, 'id', request.form['pro_id'])
    job = get_model_by_field(db, Job, 'id', request.form['job_id'])
    proposal = Proposal(**request.form)
    db.session.add(proposal)
    pro.proposals.append(proposal)
    job.proposals.append(proposal)
    db.session.commit()
    return redirect(url_for('job', username=pro.username, job_id=job.id))


@app.route('/update_proposal', methods=['POST'])
def update_proposal():
    proposal = get_model_by_field(db, Proposal, 'id', request.form['proposal_id'])
    proposal.date_updated = datetime.now(timezone.utc)
    proposal.bid = float(request.form['bid'])
    proposal.description = request.form['description']
    db.session.merge(proposal)
    db.session.commit()
    return redirect(url_for('job', username=request.form['username'], job_id=request.form['job_id']))


# Asynchronous Post Routes with JS Fetch API
pass


# Context Processors
@app.context_processor
def utility_processor():
    def f_date(dt):
        return f'{"/".join([str(i) for i in [dt.month, dt.day, dt.year]])}'

    def f_price(price):
        return f'${price:,.2f}'

    def f_job_proposal_rng(job_proposals):
        p = 'proposals'
        if job_proposals <= 5:
            display = f'0 - 5 {p}'
        elif job_proposals <= 10:
            display = f'6 - 10 {p}'
        elif job_proposals <= 15:
            display = f'11 - 15 {p}'
        elif job_proposals <= 20:
            display = f'16 - 20 {p}'
        elif job_proposals <= 25:
            display = f'21 - 25 {p}'
        else:
            display = f'More than 25 {p}'
        return display

    def f_time_since(initial_dt, prefix='Posted'):
        delta = (datetime.now(timezone.utc) - initial_dt)
        if delta.days >= 2:
            display = f'{prefix} {delta.days} days ago'
        elif delta.days >= 1:
            display = f'{prefix} {delta.days} day ago'
        else:
            if delta.seconds >= 7200:
                display = f'{prefix} {delta.seconds // 3600} hours ago'
            elif delta.seconds >= 3600:
                display = f'{prefix} {delta.seconds // 3600} hour ago'
            else:
                if delta.seconds >= 120:
                    display = f'{prefix} {delta.seconds // 60} minutes ago'
                else:
                    display = f'{prefix} {delta.seconds // 60} minute ago'
        return display

    return dict(f_date=f_date, f_price=f_price, f_job_proposal_rng=f_job_proposal_rng, f_time_since=f_time_since)







