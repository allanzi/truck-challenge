from models import base_model
from flask_pymongo import ObjectId
from jsonmerge import merge
import datetime

class TerminalModel:
    def __init__(self):
        self.terminal = base_model.mongo.db.terminal
        self.user = base_model.mongo.db.user

    def transform(self, terminal):
        return {
            'id': str(terminal['_id']),
            'user_id': terminal['user_id'],
            'is_busy': terminal['is_busy'],
            'is_active': terminal['is_active'],
            'created_at': terminal['created_at'].timestamp(),
            'updated_at': terminal['updated_at'].timestamp()
        }

    def create(self, terminal):
        try:
            user = self.user.find_one({ '_id': ObjectId(terminal['user_id']), 'is_active': True })

            if user is None:
                raise Exception('This user does not exists!')
        
            defaultData = {
                'is_active': True,
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            }
            createData = merge(terminal, defaultData)
            
            id = self.terminal.insert(createData)

            return self.terminal.find_one({ '_id': id })
        except Exception as e:
            return False

    def findDailyReport(self, period, fieldName):
        return self.terminal.aggregate([
            {
                '$project':
                {
                    'month': { '$dateToString': { 'format': period, 'date': '$created_at' } },
                }
            },
            {
                '$group': {
                    '_id': { 'created_at': '$month'},
                    'trucks': { '$sum': 1 }
                }
            },
            {
                '$addFields': {
                    fieldName: '$_id.created_at'
                }
            },
            {
                '$project': {
                    '_id': False
                }
            }
        ])