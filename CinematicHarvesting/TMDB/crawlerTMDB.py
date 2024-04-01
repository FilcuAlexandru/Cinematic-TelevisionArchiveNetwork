import aiohttp
import asyncio
import json
import os
import time
from alive_progress import alive_bar

class crawlerTMDB:
    """Class for scraping movie data from the TMDb API."""

    def __init__(self, api_key):
        """
        Initialize the crawlerTMDB object with the provided API key.

        Parameters:
        - api_key (str): The API key for accessing the TMDb API.
        """
        self.api_key = api_key

    async def fetch_movie_details(self, session, movie_id):
        """
        Fetch details for a specific movie from the TMDb API.

        Parameters:
        - session (aiohttp.ClientSession): An aiohttp client session.
        - movie_id (int): The ID of the movie to fetch details for.

        Returns:
        - dict: The details of the movie as a dictionary.
        """
        base_url = "https://api.themoviedb.org/3"
        movie_endpoint = f"/movie/{movie_id}"
        params = {"api_key": self.api_key}

        async with session.get(base_url + movie_endpoint, params=params) as response:
            try:
                response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
                data = await response.json()
                return data
            except aiohttp.ClientResponseError as e:
                print(f"Error fetching details for movie ID {movie_id}: {e}")
                return None

    async def fetch_popular_movies(self, session, page=1):
        """
        Fetch popular movies from the TMDb API.

        Parameters:
        - session (aiohttp.ClientSession): An aiohttp client session.
        - page (int): The page number of the popular movies to fetch.

        Returns:
        - list: A list of popular movies as dictionaries.
        """
        base_url = "https://api.themoviedb.org/3"
        popular_movies_endpoint = "/discover/movie"
        params = {
            "api_key": self.api_key,
            "page": page,
            "include_adult": "false",  # Convert boolean to string
        }

        async with session.get(base_url + popular_movies_endpoint, params=params) as response:
            try:
                response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
                data = await response.json()
                return data.get("results", [])
            except aiohttp.ClientResponseError as e:
                print(f"Error fetching popular movies on page {page}: {e}")
                return []

    async def scrape_all_movies(self, output_folder):
        """
        Scrape data for all movies from the TMDb API and save them to a JSON file.

        Parameters:
        - output_folder (str): The folder path where the JSON file will be saved.
        """
        all_movie_data = {}
        page = 1
        max_pages = 450  # Limit the scraping to 450 pages

        # Initialize variables for progress tracking
        start_time = time.time()
        total_movies = 0

        # Create the progress bar outside the loop
        with alive_bar(title="Fetching Movies") as bar:
            async with aiohttp.ClientSession() as session:
                while page <= max_pages:
                    popular_movies = await self.fetch_popular_movies(session, page)
                    if not popular_movies:
                        break

                    # Update total number of movies
                    total_movies += len(popular_movies)

                    # Fetch details for each movie asynchronously
                    tasks = [self.fetch_movie_details(session, movie["id"]) for movie in popular_movies]
                    movie_details = await asyncio.gather(*tasks)

                    # Add fetched movie details to the dictionary
                    for movie_id, movie_data in zip([movie["id"] for movie in popular_movies], movie_details):
                        if movie_data:
                            all_movie_data[movie_id] = movie_data

                    # Update progress bar description
                    elapsed_time = time.time() - start_time
                    bar.text("Page: {}, Movies: {}, Elapsed: {:.1f}s".format(page, total_movies, elapsed_time))
                    bar()

                    # Move to the next page
                    page += 1

        # Save all scraped data to a single JSON file
        self.save_to_json(all_movie_data, output_folder)

    def save_to_json(self, data, output_folder):
        """
        Save the scraped movie data to a JSON file.

        Parameters:
        - data (dict): The movie data to be saved.
        - output_folder (str): The folder path where the JSON file will be saved.
        """
        output_file = os.path.join(output_folder, 'tmdb_movies.json')
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Scraped data saved to {output_file}")

# TMDb API key
api_key = "98ab59ec1857b40a9d72cafd8efcb209"

# Create an instance of crawlerTMDB
crawler = crawlerTMDB(api_key)

# Scrape data for all movies and save them after scraping all data
output_folder = 'Database/JSONS'
asyncio.run(crawler.scrape_all_movies(output_folder))
