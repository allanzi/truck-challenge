from flask_restful import Resource
from flask import jsonify, make_response, request
from models.user_model import UserModel
from validators.user_validator import UserCreateValidator, UserUpdateValidator
from marshmallow import ValidationError

class UserShow(Resource):
    def __init__(self):
        self.model = UserModel()
        self.validator = UserUpdateValidator()
        super().__init__()

    def get(self, id):
        response = self.model.findById(id)

        if response is None:
            return make_response({
                'message': 'This user does not exists!'
            }, 404)

        return jsonify({
            'data': self.model.transform(response)
        })

    def delete(self, id):
        response = self.model.remove(id)

        if response is False:
            return make_response({
                'message': 'This user does not exists!'
            }, 404)

        return make_response('', 204)

    def put(self, id):
        try:
            data = request.json
            user = self.validator.load(data)
            updateduser = self.model.update(id, user)

            if updateduser is False:
                return make_response({
                    'message': 'This user does not exists!'
                }, 404)

            return make_response(
                jsonify({
                    'data': self.model.transform(updateduser)
                }), 200)
        except ValidationError as err:
            return make_response({
                'message': 'Bad request!',
                'errors': err.messages
            }, 400)
    
class UserCreateAndList(Resource):
    def __init__(self):
        self.validator = UserCreateValidator()
        self.model = UserModel()
        super().__init__()

    def get(self):
        response = []
        users = self.model.findAll()
        
        for user in users:
            response.append(self.model.transform(user))

        return jsonify({
            'data': response
        })
    
    def post(self):
        try:
            data = request.json
            user = self.validator.load(data)
            createdUser = self.model.create(user)

            return make_response(
                jsonify({
                    'data': self.model.transform(createdUser)
                }), 201)
        except ValidationError as err:
            return make_response({
                'message': 'Bad request!',
                'errors': err.messages
            }, 400)