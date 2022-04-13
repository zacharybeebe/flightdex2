from flightdex2_app.models import *
from flightdex2_app.fake_data.fake_funcs import *
from flightdex2_app.config.app_config import BASE_PRO, BASE_CLIENT


def generate_fake_data(db, number_of_users=35, jobs_per_client=5, friends=5, conversations=5):
    pro = User(**BASE_PRO)
    client = User(**BASE_CLIENT)
    pro.friends.append(client)
    client.friends.append(pro)

    users = [pro, client]
    for i in range(1, number_of_users + 1):
        user = User(**fake_user(i))
        user.friends.append(pro)
        user.friends.append(client)
        users.append(user)
    print(users)
    db.session.add_all(users)
    db.session.commit()

    for user in users[2:]:
        for _ in range(friends):
            while True:
                friend = choice(users[2:])
                if friend != user and friend not in user.friends:
                    break
            user.friends.append(friend)
            friend.friends.append(user)
    print('Completed Friends')
    db.session.commit()
    _add_address_bank_cards(db, users)
    print('Completed Address, Bank, Card')
    _add_conversations(db, users, conversations)
    print('Completed Conversations')
    _add_jobs(db, users, jobs_per_client)
    print('Completed Jobs')
    db.session.commit()


def _add_address_bank_cards(db, users):
    for user in users:
        address = Address(**fake_address())
        bank = Bank(**fake_bank())
        card = Card(**fake_card(f'{user.f_name} {user.l_name}'))
        db.session.add_all([address, bank, card])
        card.address = address
        user.address = address
        user.banks.append(bank)
        user.cards.append(card)
    db.session.commit()


def _add_conversations(db, users, conversations):
    for user in users:
        for _ in range(conversations):
            while True:
                other = choice([choice(user.friends), choice(users)])
                if other != user:
                    break
            c_kwargs, m_user, m_other = fake_conversation()
            conv = Conversation(userA_id=user.id, userB_id=other.id, **c_kwargs)
            db.session.add(conv)
            for um_kwargs, om_kwargs in zip(m_user, m_other):
                message = Message(sender_id=user.id, receiver_id=other.id, **um_kwargs)
                db.session.add(message)
                conv.messages.append(message)
                message = Message(sender_id=other.id, receiver_id=user.id, **om_kwargs)
                db.session.add(message)
                conv.messages.append(message)
            user.conversations.append(conv)
            other.conversations.append(conv)
    db.session.commit()


def _add_jobs(db, users, jobs_per_client):
        clients = [user for user in users if user.type == 'Drone Client']
        pros = [user for user in users if user.type == 'Drone Pro']

        fake_id = 1
        for client in clients:
            for _ in range(jobs_per_client):
                job = Job(client_id=client.id, **fake_job())
                address = Address(**fake_address(job.state))
                db.session.add_all([job, address])
                job.address = address
                print(f'{job=}')
                if job.status == 'posted':
                    for _ in range(randrange(0, 8)):
                        while True:
                            pro = choice(pros)
                            if job not in pro.jobs:
                                break
                        pro.jobs.append(job)
                        if choice([0, 1]) == 0:
                            proposal = Proposal(pro_id=pro.id, job_id=fake_id,  # Fake id is used to speed up data population rather than db.commit()
                                               **fake_proposal(job.project_price if job.project_price is not None else job.hourly_price))
                            db.session.add(proposal)
                            pro.proposals.append(proposal)
                            job.proposals.append(proposal)
                elif job.status in ['scheduled', 'completed']:
                    pro = choice(pros)
                    job.pro_id = pro.id
                    pro.jobs.append(job)
                client.jobs.append(job)
                fake_id += 1
        db.session.commit()








