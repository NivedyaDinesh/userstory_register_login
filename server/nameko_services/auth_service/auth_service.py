from nameko.rpc import rpc
import bcrypt
from mongodbsingleton import MongoDBSingleton

class AuthService:
    name = "auth_service"

    def __init__(self):
        # Use the MongoDBSingleton to get the database connection
        mongodb_instance = MongoDBSingleton.get_instance()
        self.mongo = mongodb_instance.mongo

    @rpc
    def sign_up(self, data):
        collection =self.mongo['users']
        # Hash the password
        password = data.get('password').encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        # Replace plain password with hashed password
        data['password'] = hashed
        result = collection.insert_one(data)
        return {'status': 'success', 'inserted_id': str(result.inserted_id)}

    @rpc
    def log_in(self, data):
        collection = self.mongo['users']
        username = data.get('username')
        password = data.get('password').encode('utf-8')
        user = collection.find_one({'username': username})
        if user and bcrypt.checkpw(password, user['password']):
            return {
                'status': 'success',
                'user_id': str(user['_id']),
                'username': user['username']
            }
        else:
            return {'status': 'failure', 'message': 'Invalid username or password'}