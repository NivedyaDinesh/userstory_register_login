from pymongo import MongoClient
from dotenv import load_dotenv
import os

class MongoDBSingleton:
    """Creates the mongoDB instance globally.
    Attributes:
        client (MongoClient): MongoDB client instance.
        mongo (Database): MongoDB database instance.
    """
    _instance = None

    def __init__(self):
        """Constructor"""
        if not MongoDBSingleton._instance:
            MongoDBSingleton._instance = self
            self._connect()

    def _connect(self):
        """Establishing mongodb connection."""
        try:
            if not hasattr(self, 'client') or not self.client:
                load_dotenv()
                self.mongo_uri = os.getenv('MONGO_URI')
                self.database_name = os.getenv('MONGODB_DATABASE')
                self.client = MongoClient(self.mongo_uri)
                self.mongo = self.client[self.database_name]
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise

    def get_collection(self, collection_name):
        """Get a specific collection from the database."""
        return self.mongo[collection_name]

    @classmethod
    def get_instance(cls):
        """Get the singleton instance of MongoDBSingleton."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance