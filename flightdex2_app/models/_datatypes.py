from flightdex2_app.config.app_config import FERNET_KEY
from cryptography.fernet import Fernet
from datetime import (
    datetime,
    timezone
)
from pickle import (
    dumps,
    loads
)
from hashlib import sha256
from sqlalchemy.types import (
    TypeDecorator,
    LargeBinary,
    String,
    DateTime
)


class Blob(TypeDecorator):
    impl = LargeBinary

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = loads(value)
        return value


class UTCDateTime(TypeDecorator):
    impl = DateTime

    def process_bind_param(self, value, engine):
        if value is None:
            return
        if value.utcoffset() is None:
            raise ValueError('Got naive datetime while timezone-aware is expected')
        return value.astimezone(timezone.utc)

    def process_result_value(self, value, engine):
        if value is not None:
            value = value.replace(tzinfo=timezone.utc)
        return value


class Password(TypeDecorator):
    impl = String(64)

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = sha256(value.encode('utf-8')).hexdigest()
        return value

    def process_result_value(self, value, dialect):
        return value


class Encrypted(TypeDecorator):
    impl = LargeBinary

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = Fernet(FERNET_KEY).encrypt(str(value).encode('utf-8'))
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            return Fernet(FERNET_KEY).decrypt(value).decode('utf-8')