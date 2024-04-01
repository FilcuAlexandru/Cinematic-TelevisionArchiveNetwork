###################################################################
#                                                                 #
#         '' crawlerThrillerTVSeries.py Documentation. ''         #
# crawlerThrillerTVSeries.py harvest thriller tv-series from IMDB #
#                                                                 #
###################################################################

##########################################
#                                        #
# crawlerThrillerTVSeries.py handy tools #
#                                        #
##########################################

import requests
from bs4 import BeautifulSoup
import json
import os

###############################################################
#                                                             #
# crawlerThrillerTVSeries.py ScrapeIMDBthrillerTVSeries class #
#     'Run the scrapping of IMDB thriller tv-series'          #
#                                                             #  
###############################################################

class ScrapeIMDBThrillerTVSeries:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept-Language': 'en-US,en;q=0.9'
        }
    
    def scrape_thriller_tvseries(self, url, output_folder):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an exception for bad responses
            soup = BeautifulSoup(response.content, "html.parser")

            # Find all list items containing TV series information
            tv_series_items = soup.find_all('li', class_='ipc-metadata-list-summary-item')

            # Initialize list to store TV series data
            tv_series = []

            # Iterate over each TV series item and extract relevant information
            for item in tv_series_items:
                try:
                    # Extract title and remove numbering
                    title = item.find('h3', class_='ipc-title__text').get_text(strip=True).split('. ', 1)[-1]

                    # Extract metadata items
                    metadata_items = item.find_all('span', class_='sc-b0691f29-8 ilsLEX dli-title-metadata-item')
                    metadata = [tag.get_text(strip=True) for tag in metadata_items]

                    # Extract year, runtime, rated, and IMDb rating from metadata
                    year = metadata[0] if len(metadata) > 0 else "N/A"
                    runtime = metadata[1] if len(metadata) > 1 else "N/A"
                    rated = metadata[2] if len(metadata) > 2 else "N/A"
                    
                    # IMDb rating may not always be present, so we need to handle that case
                    imdb_rating_element = item.find('span', class_='ipc-rating-star--imdb')
                    imdb_rating = imdb_rating_element.text.strip().split()[0] if imdb_rating_element else "N/A"

                    # Append the TV series data to the list
                    tv_series.append({
                        'title': title,
                        'year': year,
                        'runtime': runtime,
                        'rated': rated,
                        'imdb_rating': imdb_rating
                    })
                    
                    # Print the TV series data
                    print(f"Title: {title}, Year: {year}, Runtime: {runtime}, Rated: {rated}, IMDb Rating: {imdb_rating}")
                    
                except Exception as e:
                    print(f"Error occurred while parsing TV series information: {e}")
                    continue

            # Save the extracted data to a JSON file in the specified folder
            output_file = os.path.join(output_folder, 'thriller_tvseries.json')
            with open(output_file, 'w') as json_file:
                json.dump(tv_series, json_file, indent=4)
            print(f"Scraped data saved to {output_file}")
            
        except Exception as e:
            print(f"Error occurred while fetching or parsing the webpage: {e}")

# Usage example:
scraper = ScrapeIMDBThrillerTVSeries()
url = 'https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres=thriller'
output_folder = 'Database/JSONS'
scraper.scrape_thriller_tvseries(url, output_folder)






