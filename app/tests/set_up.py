import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import config
from routes.routes import configRoutes

configRoutes(config)

app = config.app
api = config.api