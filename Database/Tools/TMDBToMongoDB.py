import os
import json
from pymongo import MongoClient
import time

class TMDBToMongoDB:
    def __init__(self, mongo_uri, db_name, collection_name):
        self.client = None
        self.db = None
        self.collection = None
        self.mongo_uri = mongo_uri
        self.db_name = db_name
        self.collection_name = collection_name

    def connect_to_mongodb(self):
        connected = False
        retries = 0
        while not connected and retries < 5:  # Retry for a maximum of 5 times
            try:
                self.client = MongoClient(self.mongo_uri)
                self.db = self.client[self.db_name]
                self.collection = self.db[self.collection_name]
                connected = True
            except Exception as e:
                print(f"Failed to connect to MongoDB: {e}")
                retries += 1
                time.sleep(5)  # Wait for 5 seconds before retrying
        if not connected:
            raise Exception("Failed to connect to MongoDB after multiple retries")

    def insert_data_from_json(self, json_folder):
        file_path = os.path.join(json_folder, 'tmdb_movies.json')
        with open(file_path) as f:
            data = json.load(f)
            if isinstance(data, dict):
                data = [data]
            self.collection.insert_many(data)
            print(f"Data from {file_path} inserted into MongoDB")

# Usage example:
if __name__ == "__main__":
    json_folder = 'Database/JSONS'  # Absolute path to JSON folder
    mongo_uri = 'localhost:27017'
    db_name = 'cinematic'  
    collection_name = 'tmdb_collection'  

    tmdb_to_mongo = TMDBToMongoDB(mongo_uri, db_name, collection_name)
    tmdb_to_mongo.connect_to_mongodb()
    tmdb_to_mongo.insert_data_from_json(json_folder)