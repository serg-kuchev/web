import hashlib
from datetime import datetime

from sqlalchemy import exc

import config
import errors
from app import db


class BaseModelMixin:

    @classmethod
    def by_id(cls, obj_id):
        obj = cls.query.get(obj_id)
        if obj:
            return obj
        else:
            raise errors.NotFound

    def add(self):
        db.session.add(self)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.BadRequest


class User(db.Model, BaseModelMixin):

    __tablename__ = 'Пользователь'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nulltable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    ad = db.relationship('Ad', backref='user')

    def __str__(self):
        return '<User {}>'.format(self.username)

    def __repr__(self):
        return str(self)

    def set_password(self, raw_password: str):
        raw_password = f'{raw_password}{config.SALT}'
        self.password = hashlib.md5(raw_password.encode()).hexdigest()

    def check_password(self, raw_password: str):
        raw_password = f'{raw_password}{config.SALT}'
        return self.password == hashlib.md5(raw_password.encode()).hexdigest()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            "email": self.email
        }


class Ad(db.Model, BaseModelMixin):

    __tablename__ = 'Объявление'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True, nullable=False)
    description = db.Column(db.Text, index=True)
    creator_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

    def __str__(self):
        return '<Ad {}>'.format(self.username)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            "description": self.description,
            'creator_id': self.creator_id,
            'created_on': self.created_on

        }
