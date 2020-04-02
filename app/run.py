import config
from routes import routes
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/api/docs/json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "TruckPad Challenge"
    }
)

config.app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

config.app.run(host='0.0.0.0', debug=True)