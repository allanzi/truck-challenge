from models import base_model
from flask_pymongo import ObjectId
from werkzeug.exceptions import NotFound
from jsonmerge import merge
import datetime

class TravelModel:
    def __init__(self):
        self.travel = base_model.mongo.db.travel
        self.user = base_model.mongo.db.user

    def transform(self, travel):
        return {
            'id': str(travel['_id']),
            'user_id': travel['user_id'],
            'from': travel['from_'],
            'to': travel['to'],
            'created_at': travel['created_at'].timestamp(),
            'updated_at': travel['updated_at'].timestamp()
        }

    def findById(self, id):
        return self.travel.find_one({ '_id': ObjectId(id), 'is_active': True })

    def remove(self, id):
        if self.findById(id) is None:
            return False

        self.update(id, { 'is_active': False })

        return True

    def findAll(self):
        return self.travel.find({ 'is_active': True })

    def create(self, travel):
        try:
            user = self.user.find_one({ '_id': ObjectId(travel['user_id']), 'is_active': True });

            if user is None:
                raise Exception('This user does not exists!')
        
            defaultData = {
                'is_active': True,
                'created_at': datetime.datetime.utcnow(),
                'updated_at': datetime.datetime.utcnow()
            }
            createData = merge(travel, defaultData)
            
            id = self.travel.insert(createData)

            return self.travel.find_one({ '_id': id })
        except Exception:
            return False
        
    def update(self, id, travel):
        try:
            if self.findById(id) is None:
                raise NotFound()

            updateData = merge(travel, { 'updated_at': datetime.datetime.utcnow() })

            if 'user_id' in travel:
                user = self.user.find_one({ '_id': ObjectId(travel['user_id']), 'is_active': True })
                if user is None:
                    raise Exception('This user does not exists!')

            self.travel.update(
                { '_id': ObjectId(id) },
                {
                    '$set': updateData
                }
            )

            return self.findById(id)
        except Exception:
            return False

    def findTravelPerUsersReport(self):
        return self.travel.aggregate([
        {
            '$group': {
                '_id': {
                    'user_id': '$user_id'
                },
                'travels': {
                    '$push': {
                        'to': '$to', 
                        'from': '$from_'
                    }
                }
            }
        },
    ])