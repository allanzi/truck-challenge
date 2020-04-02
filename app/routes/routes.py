import config
from controllers.user_controller import UserShow
from controllers.doc_controller import DocController

config.api.add_resource(UserShow, '/api/users/<string:name>')
config.api.add_resource(DocController, '/api/docs/json')