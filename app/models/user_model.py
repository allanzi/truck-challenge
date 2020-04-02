from models import base_model
import datetime

class UserModel:
    def __init__(self):
        self.user = base_model.mongo.db.user

    def transform(self, user):
        return {
            'id': str(user['_id']),
            'name': user['name'],
            'is_active': user['is_active'],
            'created_at': user['created_at'].timestamp(),
            'updated_at': user['updated_at'].timestamp()
        }

    def findByName(self, name):
        return self.user.find_one({'name': name})

    def create(self, user):
        id = self.user.insert({ 
            'name': user['name'], 
            'is_active': True,
            'created_at': datetime.datetime.utcnow(),
            'updated_at': datetime.datetime.utcnow()
        })

        return self.user.find_one({ '_id': id })
