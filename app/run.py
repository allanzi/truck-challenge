import config
from routes.routes import configRoutes

configRoutes(config)

config.app.run(host='0.0.0.0', debug=True)