import subprocess
import os
import logging

class FetchAndInsertIMDB:
    def __init__(self):
        self.movies_crawlers_dir = "CinematicHarvesting\IMDB\Movies\Crawlers"
        self.tv_series_crawlers_dir = "CinematicHarvesting\IMDB\TVSeries\Crawlers"
        self.imdb_to_mongodb_script = "Database\Tools\IMDBToMongoDB.py"

    def run_imdb_crawlers(self, crawlers_dir):
        crawlers = os.listdir(crawlers_dir)
        for crawler in crawlers:
            if crawler.startswith("crawler") and crawler.endswith(".py"):
                crawler_path = os.path.join(crawlers_dir, crawler)
                subprocess.run(["python", crawler_path])

    def run_imdb_to_mongodb(self):
        subprocess.run(["python", self.imdb_to_mongodb_script])

    def main(self):
        try:
            # Run movie crawlers
            self.run_imdb_crawlers(self.movies_crawlers_dir)
            
            # Run TV series crawlers
            self.run_imdb_crawlers(self.tv_series_crawlers_dir)
            
            self.run_imdb_to_mongodb()
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_and_insert_imdb = FetchAndInsertIMDB()
    fetch_and_insert_imdb.main()
