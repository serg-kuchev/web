from flask import jsonify
from flask_restful import Resource, reqparse

from models import User

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        user = User(**data)
        user.set_password(data['password'])
        user.add()
        return jsonify(user.to_dict())


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        return data


class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}