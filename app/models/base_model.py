from os import getenv
from flask_pymongo import PyMongo

import sys
import config

config.app.config['MONGO_DBNAME'] = getenv('DB_DATABASE')
config.app.config['MONGO_URI'] = getenv('DB_HOST')

mongo = PyMongo(config.app)