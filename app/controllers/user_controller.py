from flask_restful import Resource
from flask import jsonify, make_response, request
from models.user_model import UserModel
from validators.user_validator import UserValidator
from marshmallow import ValidationError

class UserShow(Resource):
    def __init__(self):
        self.model = UserModel()
        super().__init__()

    def get(self, name):
        response = self.model.findByName(name)

        if response is None:
            return make_response({
                'message': 'This user does not exists!'
            }, 404)

        return jsonify({
            'data': self.model.transform(response)
        })
    
class UserCreateAndList(Resource):
    def __init__(self):
        self.validator = UserValidator()
        self.model = UserModel()
        super().__init__()

    def post(self):
        try:
            data = request.json
            user = self.validator.load(data)
            createdUser = self.model.create(user)

            return jsonify({
                'data': self.model.transform(createdUser)
            })
        except ValidationError as err:
            return make_response({
                'message': 'Bad request!',
                'errors': err.messages
            }, 400)