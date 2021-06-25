from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

import config


aplication = Flask(__name__)
aplication.config.from_mapping(config.CONFIG)
db = SQLAlchemy(aplication)

api = Api(aplication)


if __name__ == '__main__':
    aplication.run(port=8082, debug=True)
