from cryptography.fernet import Fernet

FERNET_KEY = b'uhwpTEYs8yAsEPnPjVqoZqOlw2svERU7-nGJFrDsfjs='
SECRET_KEY = """D3"k~N8vq80472aE3u6612~=6>b*4#8H"""
SQLALCHEMY_DATABASE_URI = 'sqlite:///flightdex2_db.db'
# SQLALCHEMY_DATABASE_URI = 'postgresql://<your_username>:<your_password>@<host>:<port>/<database_name>'
# SQLALCHEMY_DATABASE_URI = 'mysql://<your_username>:<your_password>@<host>:<port>/<database_name>
# SQLALCHEMY_DATABASE_URI = 'oracle://<your_username>:<your_password>@<host>:<port>/<sid_name>


BASE_PRO = {
    'f_name': 'Zach',
    'l_name': 'Beebe',
    'email': 'zach.beebe.pro@flight-dex.com',
    'phone': '425-931-8214',
    'company': 'FlightDex',
    'state': 'Washington',
    'metro': 'Seattle-Tacoma-Bellevue',
    'username': 'fdpro',
    'password': 'fdpro',
    'type': 'Drone Pro'
}

BASE_CLIENT = {
    'f_name': 'Zach',
    'l_name': 'Beebe',
    'email': 'zach.beebe.client@flight-dex.com',
    'phone': '425-931-8214',
    'company': 'FlightDex',
    'state': 'Washington',
    'metro': 'Seattle-Tacoma-Bellevue',
    'username': 'fdclient',
    'password': 'fdclient',
    'type': 'Drone Client'
}
