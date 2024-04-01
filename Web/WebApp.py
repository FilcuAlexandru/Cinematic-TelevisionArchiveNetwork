import streamlit as st
import pandas as pd
from pymongo import MongoClient

# MongoDB connection details
mongo_uri = 'localhost:27017'
db_name = 'cinematic'
collection_names = [
    'imdb_action_movies_collection',
    'imdb_action_tvseries_collection',
    'imdb_horror_movies_collection', 
    'imdb_horror_tvseries_collection',
    'imdb_musical_movies_collection',
    'imdb_musical_tvseries_collection',
    'imdb_romance_movies_collection',
    'imdb_romance_tvseries_collection',
    'imdb_scifi_movies_collection',
    'imdb_scifi_tvseries_collection',
    'imdb_sport_movies_collection',
    'imdb_sport_tvseries_collection',
    'imdb_thriller_movies_collection',
    'imdb_thriller_tvseries_collection',
    'imdb_western_movies_collection',
    'imdb_western_tvseries_collection'
]

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[db_name]

def create_dataframe(collection_name):
    # Retrieve data from MongoDB
    collection = db[collection_name]
    data = collection.find()

    # Create DataFrame
    df = pd.DataFrame(list(data))

    # Drop the _id column
    df.drop('_id', axis=1, inplace=True)

    # Change index to start from 1
    df.index += 1

    return df

def main():
    st.title("Cinematic Data from IMDB")

    # Iterate over collection names
    for collection_name in collection_names:
        # Create DataFrame for each collection
        df = create_dataframe(collection_name)

        # Display title for the DataFrame
        st.subheader(f"Analyse {collection_name}")

        # Display DataFrame in Streamlit
        st.write(df)

if __name__ == "__main__":
    main()
