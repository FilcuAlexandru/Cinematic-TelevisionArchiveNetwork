import subprocess
import os
import logging

class FetchAndInsertData:
    def __init__(self, crawler_script, to_mongodb_script):
        self.crawler_script = crawler_script
        self.to_mongodb_script = to_mongodb_script

    def run_crawler(self):
        subprocess.run(["python", self.crawler_script])

    def run_to_mongodb(self):
        subprocess.run(["python", self.to_mongodb_script])

    def main(self):
        try:
            self.run_crawler()
            self.run_to_mongodb()
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # IMDB Configuration
    imdb_crawlers_dir = "CinematicHarvesting\IMDB\Movies\Crawlers"
    imdb_to_mongodb_script = "Database\Tools\IMDBToMongoDB.py"

    imdb_crawlers = os.listdir(imdb_crawlers_dir)
    for crawler in imdb_crawlers:
        if crawler.startswith("crawler") and crawler.endswith(".py"):
            crawler_path = os.path.join(imdb_crawlers_dir, crawler)
            fetch_and_insert_imdb = FetchAndInsertData(crawler_path, imdb_to_mongodb_script)
            fetch_and_insert_imdb.main()

    # TMDB Configuration
    tmdb_crawler_script = "CinematicHarvesting\TMDB\crawlerTMDB.py"
    tmdb_to_mongodb_script = "Database\Tools\TMDBToMongoDB.py"

    fetch_and_insert_tmdb = FetchAndInsertData(tmdb_crawler_script, tmdb_to_mongodb_script)
    fetch_and_insert_tmdb.main()

    # Starting Streamlit app
    streamlit_app_path = "Web\WebApp.py"
    subprocess.run(["python", "-m", "streamlit", "run", streamlit_app_path])
