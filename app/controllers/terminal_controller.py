from flask_restful import Resource
from flask import jsonify, make_response, request
from models.terminal_model import TerminalModel
from validators.terminal_validator import TerminalCreateValidator
from marshmallow import ValidationError

class TerminalController(Resource):
    def __init__(self):
        self.model = TerminalModel()
        self.validator = TerminalCreateValidator()
        super().__init__()

    def post(self):
        try:
            data = request.json
            terminal = self.validator.load(data)
            createdTerminal = self.model.create(terminal)

            if createdTerminal is False:
                return make_response({
                    'message': 'Bad request!',
                    'errors': {
                        'user_id': [
                        'Must be a valid ObjectId or Not found.'
                        ]
                    }
                }, 400)

            return make_response(
                jsonify({
                    'data': self.model.transform(createdTerminal)
                }), 201)
        except ValidationError as err:
            return make_response({
                'message': 'Bad request!',
                'errors': err.messages
            }, 400)