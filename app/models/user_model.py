from models import base_model
from flask_pymongo import ObjectId
from jsonmerge import merge
import datetime

class UserModel:
    def __init__(self):
        self.user = base_model.mongo.db.user

    def transform(self, user):
        return {
            'id': str(user['_id']),
            'name': user['name'],
            'age': user['age'],
            'has_vehicle': user['has_vehicle'],
            'driver_license_type': user['driver_license_type'],
            'is_busy': user['is_busy'],
            'vehicle_type_id': user['vehicle_type_id'],
            'is_active': user['is_active'],
            'created_at': user['created_at'].timestamp(),
            'updated_at': user['updated_at'].timestamp()
        }

    def findAllIsbusy(self):
        return self.user.find({ 'is_busy': False, 'is_active': True })

    def findAllHasOwnVehicle(self):
        return self.user.find({ 'has_vehicle': True, 'is_active': True })

    def findById(self, id):
        return self.user.find_one({ '_id': ObjectId(id), 'is_active': True })

    def remove(self, id):
        if self.findById(id) is None:
            return False

        self.update(id, { 'is_active': False })

        return True

    def findAll(self):
        return self.user.find({ 'is_active': True })

    def create(self, user):
        defaultData = {
            'is_active': True,
            'created_at': datetime.datetime.utcnow(),
            'updated_at': datetime.datetime.utcnow()
        }
        createData = merge(user, defaultData)
        
        id = self.user.insert(createData)

        return self.user.find_one({ '_id': id })
        
    def update(self, id, user):
        updateData = merge(user, { 'updated_at': datetime.datetime.utcnow() })

        if self.findById(id) is None:
            return False
        
        self.user.update(
            { '_id': ObjectId(id) },
            {
                '$set': updateData
            }
        )

        return self.findById(id)
