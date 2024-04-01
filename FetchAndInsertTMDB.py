import subprocess
import os
import logging

class FetchAndInsertTMDB:
    def __init__(self):
        self.crawler_script = "CinematicHarvesting\TMDB\crawlerTMDB.py"
        self.tmdb_to_mongodb_script = "Database\Tools\TMDBToMongoDB.py"

    def run_tmdb_crawler(self):
        subprocess.run(["python", self.crawler_script])

    def run_tmdb_to_mongodb(self):
        subprocess.run(["python", self.tmdb_to_mongodb_script])

    def main(self):
        try:
            self.run_tmdb_crawler()
            self.run_tmdb_to_mongodb()
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_and_insert_tmdb = FetchAndInsertTMDB()
    fetch_and_insert_tmdb.main()
