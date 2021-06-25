from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from resources import UserLogin, UserRegistration, UserLogoutAccess, UserLogoutRefresh

import config


app = Flask(__name__)
app.config.from_mapping(config.CONFIG)
db = SQLAlchemy(app)

api = Api(app)

api.add_resource(UserRegistration, '/registration')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogoutAccess, '/logout/access')
api.add_resource(UserLogoutRefresh, '/logout/refresh')
