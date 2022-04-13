from datetime import date, timedelta
from faker import Faker
from faker.providers import bank, company, credit_card, person, phone_number
from random import choice, randrange
from flightdex2_app.config.constants import US_STATES, METROS, JOB_TYPES

F = Faker('en_US')
for p in [bank, company, credit_card, person, phone_number]:
    F.add_provider(p)


def printd(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')
    print()


def f_date(past=False):
    now = date.today()
    if past:
        min_date = date(2021, 1, 1)
        max_date = now

    else:
        min_date = now
        max_date = date(2023, 12, 31)
    delta = (max_date - min_date).days
    return min_date + timedelta(days=randrange(0, delta))


def f_time():
    times = []
    for i in range(8, 20):
        if i < 12:
            times.append(f'{i}:{choice(["00", "15", "30", "45"])} AM')
        elif i == 12:
            times.append(f'{i}:{choice(["00", "15", "30", "45"])} PM')
        else:
            times.append(f'{i-12}:{choice(["00", "15", "30", "45"])} PM')
    return choice(times)


def f_phone():
    two = "".join([str(randrange(1, 10)) for _ in range(3)])
    three = "".join([str(randrange(1, 10)) for _ in range(4)])
    return f'555-{two}-{three}'


def fake_address(state=None):
    kwargs = {
        'street': f'{"".join([str(randrange(1, 10)) for _ in range(choice([3, 4, 5]))])} {F.street_name()}',
        'apt': choice([None, f'# {F.building_number()}']),
        'city': F.city(),
        'state': choice(US_STATES) if state is None else state,
        'zip_code': F.postcode()
    }
    return kwargs


def fake_bank():
    kwargs = {
        'routing': F.aba(),
        'institution': f'Bank of {choice(US_STATES)}',
        'account': F.bban()
    }
    return kwargs


def fake_card(name='Fake User'):
    kwargs = {
        'name': name,
        'number': F.credit_card_number(),
        'institution': F.credit_card_provider(),
        'expiration': F.credit_card_expire(),
        'security': F.credit_card_security_code(),
        'nickname': 'Fake Nickname'
    }
    return kwargs


def fake_conversation(subject='No Subject', length=10):
    user1 = []
    user2 = []
    for i in range(1, 3):
        for _ in range(length):
            kwargs = {
                'message': F.text()
            }
            eval(f'user{i}').append(kwargs)

    return {'subject': subject}, user1, user2


def fake_job():
    bid = choice([None, 300, 600, 900, 1200, 1500])
    hourly = None
    if bid is None:
        hourly = choice([25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
    j_type = choice(list(JOB_TYPES.keys()))
    sub = choice(JOB_TYPES[j_type])
    status = choice(['posted', 'scheduled', 'completed'])
    state = choice(US_STATES)
    title = F.text()
    kwargs = {
        'type': j_type,
        'sub_type': sub,
        'status': status,
        'project_price': bid,
        'hourly_price': hourly,
        'date_target': f_date(past=True) if status == 'completed' else f_date(),
        'time': f_time(),
        'state': state,
        'metro': choice(METROS[state]),
        'title': title[:128] if len(title) > 128 else title,
        'description': F.text()
    }
    return kwargs


def fake_user(iteration=1):
    f_name = F.first_name()
    l_name = F.last_name()
    email = f"""{f_name}.{l_name}@fake.com"""
    state = choice(US_STATES)
    kwargs = {
        'f_name': f_name,
        'l_name': l_name,
        'email': email,
        'phone': f_phone(),
        'company': F.company(),
        'state': state,
        'metro': choice(METROS[state]),
        'username': f'test{iteration}',
        'password': f'test{iteration}',
        'type': choice(['Drone Pro', 'Drone Client'])
    }
    return kwargs


def fake_proposal(target_bid):
    kwargs = {
        'bid': choice([1.00, 0.975, 0.95, 0.925, 0.90]) * target_bid,
        'description': F.text()
    }
    return kwargs



if __name__ == '__main__':
    from cryptography.fernet import Fernet
    #key = Fernet.generate_key()
    key = b'uhwpTEYs8yAsEPnPjVqoZqOlw2svERU7-nGJFrDsfjs='

    print(key)
    x = 'Hello my name is Zach Beebe'
    enc = Fernet(key).encrypt(x.encode('utf-8'))
    print(enc)

    #key = Fernet.generate_key()
    dec = Fernet(key).decrypt(enc).decode('utf-8')
    print(dec)


