from controllers.user_controller import UserShow, UserCreateAndList
from controllers.doc_controller import DocController

def configRoutes(config):
    config.api.add_resource(UserShow, '/api/users/<string:name>')
    config.api.add_resource(UserCreateAndList, '/api/users')
    config.api.add_resource(DocController, '/api/docs/json')