from models import base_model

class UserModel:
    def __init__(self):
        self.user = base_model.mongo.db.user

    def findUserByName(self, name):
        return self.user.find_one({'name': name})