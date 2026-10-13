from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Connection settings for the AAC database
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        
        # User lives in the admin database (Module 3)
        self.client = MongoClient(
            HOST,
            PORT,
            username=username,
            password=password,
            authSource='admin'
        )
        self.database = self.client[DB]
        self.collection = self.database[COL]
    
    def create(self, data):
        # Insert one document. Return True if Mongo accepted it, else False.
        if data is not None:
            try: 
                result = self.collection.insert_one(data)
                return result.acknowledged
            except Exception:
                return False
        else:
            return False
        
    def read(self, query):
        # find() returns a cursor. Convert it to a list.
        # Empty list if the query fails or nothing matches.
        if query is not None:
            try: 
                return list(self.collection.find(query))
            except Exception:
                return []
        else:
            return []
        
    def update(self, query, data):
        # Change matching documents. Return how many were changed.
        if query is not None and data is not None:
            try:
                result = self.collection.update_many(query, {"$set": data})
                return result.modified_count
            except Exception:
                return 0
        else:
            return 0
        
    def delete(self, query):
        # Remove matching documents. Return how many were removed.
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception:
                return 0
        else:
            return 0