from flask_restful import Resource
from flask import jsonify, make_response, request
from models.user_model import UserModel
from models.terminal_model import TerminalModel
from models.travel_model import TravelModel
from validators.user_validator import UserCreateValidator, UserUpdateValidator
from marshmallow import ValidationError

class UsersWithouLoaded(Resource):
    def __init__(self):
        self.model = UserModel()
        super().__init__()

    def get(self):
        response = []
        users = self.model.findAllIsbusy()

        for user in users:
            response.append(self.model.transform(user))


        return jsonify({
            'data': response
        })

class UsersWithOwnVehicle(Resource):
    def __init__(self):
        self.model = UserModel()
        super().__init__()

    def get(self):
        response = []
        users = self.model.findAllHasOwnVehicle()

        for user in users:
            response.append(self.model.transform(user))


        return jsonify({
            'data': response
        })
        
class TerminalReportController(Resource):
    def __init__(self):
        self.model = TerminalModel()
        super().__init__()

    def get(self):
        daily = list(self.model.findDailyReport('%Y-%m-%d', 'date'))
        weekly = list(self.model.findDailyReport('%V', 'week'))
        monthly = list(self.model.findDailyReport('%m', 'month'))

        return jsonify({
            'data': {
                'daily': daily,
                'weekly': weekly,
                'monthly': monthly,
            }
        })
        
class TravelReportController(Resource):
    def __init__(self):
        self.model = TravelModel()
        super().__init__()

    def get(self):
        data = list(self.model.findTravelPerUsersReport())

        return jsonify({
            'data': data
        })