import os
import json
import logging
from pymongo import MongoClient

class IMDBToMongoDB:
    """A class to import data from JSON files into MongoDB."""

    def __init__(self, mongo_uri, db_name):
        """Initialize the IMDBToMongoDB instance.

        Args:
            mongo_uri (str): The MongoDB connection URI.
            db_name (str): The name of the MongoDB database.
        """
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]

    def insert_data_from_json(self, json_folder):
        """Insert data from JSON files into MongoDB collections.

        Args:
            json_folder (str): The path to the folder containing JSON files.
        """
        for file_name in os.listdir(json_folder):
            if file_name.endswith('.json') and file_name != 'tmdb_movies.json':
                file_path = os.path.join(json_folder, file_name)
                genre, media_type = file_name.split('_')[:2]
                collection_name = f'imdb_{genre}_{media_type[:-5]}_collection'  # Remove the last 5 characters (.json)
                try:
                    with open(file_path) as json_file:
                        data = json.load(json_file)
                        if isinstance(data, list) and data:
                            collection = self.db[collection_name]
                            collection.insert_many(data)
                            logging.info(f"Data from {file_name} inserted into MongoDB collection: {collection_name}")
                        else:
                            logging.warning(f"Ignoring {file_name}: Not a non-empty list of documents.")
                except Exception as e:
                    logging.error(f"Error inserting data from {file_name}: {e}")

    def close_connection(self):
        """Close the MongoDB connection."""
        self.client.close()
        logging.info("MongoDB connection closed.")

# Usage example:
if __name__ == "__main__":
    json_folder = 'Database/JSONS'
    mongo_uri = 'localhost:27017'
    db_name = 'cinematic'

    logging.basicConfig(level=logging.INFO)  # Set logging level
    json_to_mongo = IMDBToMongoDB(mongo_uri, db_name)
    json_to_mongo.insert_data_from_json(json_folder)
    json_to_mongo.close_connection()
