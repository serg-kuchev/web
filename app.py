import os

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

import config


aplication = Flask(__name__)
aplication.config.from_mapping(config.CONFIG)
db = SQLAlchemy(aplication)

api = Api(aplication)


@aplication.route('/')
def hello_world():
    return 'Moe Flask приложение.'


if __name__ == '__main__':
    aplication.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.getenv('PORT', default=5000))
    )
