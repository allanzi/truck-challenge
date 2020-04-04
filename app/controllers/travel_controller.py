from flask_restful import Resource
from flask import jsonify, make_response, request
from werkzeug.exceptions import NotFound
from models.travel_model import TravelModel
from validators.travel_validator import TravelCreateValidator, TravelUpdateValidator
from marshmallow import ValidationError

class TravelShow(Resource):
    def __init__(self):
        self.model = TravelModel()
        self.validator = TravelUpdateValidator()
        super().__init__()

    def get(self, id):
        response = self.model.findById(id)

        if response is None:
            return make_response({
                'message': 'This travel does not exists!'
            }, 404)

        return jsonify({
            'data': self.model.transform(response)
        })

    def delete(self, id):
        response = self.model.remove(id)

        if response is False:
            return make_response({
                'message': 'This travel does not exists!'
            }, 404)

        return make_response('', 204)

    def put(self, id):
        try:
            data = request.json
            travel = self.validator.load(data)
            updatedTravel = self.model.update(id, travel)

            if updatedTravel is False:
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
                    'data': self.model.transform(updatedTravel)
                }), 200)
        except ValidationError as err:
            return make_response({
                'message': 'Bad request!',
                'errors': err.messages
            }, 400)
        except NotFound as err:
            return make_response({
                'message': 'This travel does not exists!'
            }, 404)
    
class TravelCreateAndList(Resource):
    def __init__(self):
        self.validator = TravelCreateValidator()
        self.model = TravelModel()
        super().__init__()

    def get(self):
        response = []
        travels = self.model.findAll()
        
        for travel in travels:
            response.append(self.model.transform(travel))

        return jsonify({
            'data': response
        })
    
    def post(self):
        try:
            data = request.json
            travel = self.validator.load(data)
            createdTravel = self.model.create(travel)

            if createdTravel is False:
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
                    'data': self.model.transform(createdTravel)
                }), 201)
        except ValidationError as err:
            return make_response({
                'message': 'Bad request!',
                'errors': err.messages
            }, 400)