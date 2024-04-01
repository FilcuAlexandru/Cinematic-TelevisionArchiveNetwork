######################################################################                     
#                                                                    #
#    Cinematic & Television Archive Network Project Documentation    #
#                     Created by Filcu Alexandru                     #
#                                                                    #
######################################################################     

### Prerequisites
Before working with the Cinematic & Television Archive Network Project, ensure the following prerequisites are met:

- **Python Installation**: Python must be installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).
- **Python Packages**: Install the required Python packages using pip, the Python package manager:
    ```bash
    pip install requests beautifulsoup4 pymongo streamlit
    ```
    - `requests` is used for making HTTP requests to fetch data.
    - `beautifulsoup4` is utilized for parsing HTML content fetched from web pages.
    - `pymongo` is required for interfacing with MongoDB.
    - `streamlit` is used for building the web interface.
- **Access to IMDB and TMDB APIs**: Obtain API keys for accessing data from IMDB and TMDB. You can register for API keys on the respective websites:
    - [IMDB API](https://developer.imdb.com/)

- **MongoDB Installation**: MongoDB must be installed and running on your system. You can download MongoDB from the [official website](https://www.mongodb.com/try/download/community).

### Project Overview
The Cinematic & Television Archive Network Project is a comprehensive endeavor that combines various aspects of Python programming. It is tailored for enthusiasts of cinematic data, offering a centralized platform for accessing, storing, and analyzing movie and TV series information.

### Project Structure
The project is structured into the following directories:

- **CinematicHarvesting**: Contains Python scripts responsible for scraping data from IMDB and TMDB.
    - **IMDB**: Subdirectory containing scrapers for various movie and TV series genres on IMDB.
    - **TMDB**: Subdirectory containing a scraper utilizing the TMDB API key for fetching movie and TV series data.

- **Database**: Manages the storage and manipulation of data.
    - **JSONS**: Stores scraped data in JSON format.
    - **Tools**: Contains scripts for inserting data into MongoDB from the JSON files.

- **Web**: Hosts the Streamlit web application for data visualization and analysis.

- **Separate Python Scripts**:
    - **FetchAndInsertsIMDB.py**: Initiates the IMDB movie and TV series crawlers and inserts the scraped data into MongoDB.
    - **FetchAndInsertTMDB.py**: Executes the TMDB movie and TV series crawler and inserts the fetched data into MongoDB.
    - **main.py**: Orchestrates the execution of FetchAndInsertsIMDB.py, FetchAndInsertTMDB.py, and the Streamlit web app.

### Usage
1. **Data Collection**:
   - Run `FetchAndInsertsIMDB.py` to scrape IMDB data and insert it into MongoDB.
   - Run `FetchAndInsertTMDB.py` to fetch TMDB data and insert it into MongoDB.

2. **Web Interface**:
   - Execute `main.py` to start the data collection process and launch the Streamlit web app for visualization and analysis.

### Notes
- Regular updates to the project may be required to accommodate changes in IMDB and TMDB website structures or APIs.
- Ensure proper error handling and logging mechanisms are implemented to manage unforeseen issues during data scraping and analysis.
- The project can be extended to include additional features like user authentication, recommendation systems, or collaborative filtering for enhanced user experience.

The Cinematic & Television Archive Network Project aims to provide a rich and immersive experience for cinephiles, offering a comprehensive platform for exploring and analyzing cinematic data.
