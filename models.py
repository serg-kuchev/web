from datetime import datetime
import hashlib
import config

from aiohttp import web
from asyncpg import UniqueViolationError
from gino import Gino


db = Gino()


class BaseModel:

    @classmethod
    async def get_or_404(cls, obj_id):
        instance = await cls.get(obj_id)
        if instance:
            return instance
        raise web.HTTPNotFound(text='данного ID нет в базе')

    @classmethod
    async def create_instance(cls, **kwargs):
        try:
            instance = await cls.create(**kwargs)
        except UniqueViolationError:
            raise web.HTTPBadRequest()
        return instance


class User(db.Model, BaseModel):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    _idx1 = db.Index('users_user_email', 'email', unique=True)

    def __str__(self):
        return '<User {}>'.format(self.username)

    def __repr__(self):
        return str(self)

    @classmethod
    async def create_instance(cls, **kwargs):
        kwargs['password'] = hashlib.md5(kwargs['password'].encode()).hexdigest()
        return await super().create_instance(**kwargs)

    def check_password(self, raw_password: str):
        raw_password = f'{raw_password}{config.SALT}'
        return self.password == hashlib.md5(raw_password.encode()).hexdigest()

    def to_dict(self):
        user_data = super().to_dict()
        user_data.pop('password')
        return user_data


class Ad(db.Model, BaseModel):

    __tablename__ = 'advertisements'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    _idx1 = db.Index('advertisements_ad_title', 'title', unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': str(self.created_at),
            'creator_id': self.creator_id,
        }

    def __str__(self):
        return '<Advertisment {}>'.format(self.title)

    def __repr__(self):
        return str(self)
