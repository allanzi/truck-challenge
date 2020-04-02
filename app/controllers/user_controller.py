from flask_restful import Resource
from flask import jsonify, make_response
from models.user_model import UserModel

class UserShow(Resource):
    def __init__(self):
        self.model = UserModel()
        super().__init__()

    def get(self, name):
        response = self.model.findUserByName(name)

        if response is None:
            return make_response({
                'message': 'This user does not exists!'
            }, 404)

        return jsonify({
            'data': response
        })