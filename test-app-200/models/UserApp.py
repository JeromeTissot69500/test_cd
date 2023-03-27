from ..db.db import db
from datetime import datetime as dt
from sqlalchemy.ext.hybrid import hybrid_property


class UserApp(db.Model):
    __tablename__ = "users_app"
    _id_user = db.Column('id_user', db.Integer, primary_key=True)
    _assure_number = db.Column('assure_number', db.String, unique=True, nullable=False)
    _last_name = db.Column('last_name', db.String)
    _first_name = db.Column('first_name', db.String)
    _birthday = db.Column('birthday', db.DateTime)
    _address = db.Column('address', db.String)
    _phone_number = db.Column('phone_number', db.String, unique=True, nullable=False)
    _license_number = db.Column('license_number', db.String, unique=True, nullable=False)
    _email = db.Column('email', db.String, unique=True, nullable=False)
    _password = db.Column('password', db.String, unique=True, nullable=False)

    def __init__(self, id_user: int, assure_number: str, last_name: str, first_name: str, birthday: dt, address: str,
                 phone_number: str, license_number: str, email: str, password: str):
        self._id_user = id_user
        self._assure_number = assure_number
        self._last_name = last_name
        self._first_name = first_name
        self._birthday = birthday
        self._address = address
        self._phone_number = phone_number
        self._license_number = license_number
        self._email = email
        self._password = password

    # Define getter and setter property
    @hybrid_property
    def id_user(self):
        return self._id_user

    @hybrid_property
    def assure_number(self):
        return self._assure_number

    @assure_number.setter
    def assure_number(self, assure_number: str):
        self._assure_number = assure_number

    @hybrid_property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @hybrid_property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @hybrid_property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday: dt):
        self._birthday = birthday

    @hybrid_property
    def address(self):
        return self._address

    @address.setter
    def address(self, address: str):
        self._address = address

    @hybrid_property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        self._phone_number = phone_number

    @hybrid_property
    def license_number(self):
        return self._license_number

    @license_number.setter
    def license_number(self, license_number: str):
        self._license_number = license_number

    @hybrid_property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password

    @hybrid_property
    def full_name(self):
        return f"{self._last_name} {self._first_name}"
    
    @hybrid_property
    # get birthday in text
    def format_birthday(self):
        return dt.strftime(self._birthday, "%Y-%m-%d")
    
    def __repr__(self):
        return f"<UserApp: {self.email}"