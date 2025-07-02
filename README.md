# Web Scraping with Python: eBay Laptops & IMDb Movies

This repository contains two independent Python web scraping scripts: one for extracting laptop data from eBay using `requests` and `BeautifulSoup`, and another for scraping movie details from IMDb using `Selenium`.

## About the Project

This project demonstrates different approaches to web scraping based on the nature of the target website:

1.  **eBay Laptop Scraper (`ebay_laptops_scraper.py`):**
    * Utilizes `requests` for making HTTP requests to fetch static HTML content from eBay search results.
    * Employs `BeautifulSoup` for efficient parsing of the HTML and extracting structured data like laptop names, prices, shipping information, and product links.
    * Designed for websites where the data is readily available in the initial HTML response.

2.  **IMDb Movie Scraper (`imdb_movies_scraper.py`):**
    * Leverages `Selenium` for interacting with dynamic web content on IMDb. This is crucial for navigating through filters, loading "see more" buttons (AJAX content), and generally mimicking human browser behavior.
    * Collects detailed movie information such as title, release year, duration, IMDb rating, genres, director, stars, and Metascore.
    * Goes through multiple pages by clicking "more" buttons to ensure a comprehensive dataset.

Both scripts save the extracted data into an Excel file using the `pandas` library.

## Features

### eBay Laptop Scraper
* Scrapes laptop names, prices, shipping costs, and direct product links.
* Iterates through multiple pages of search results to gather more data.
* Handles missing data points gracefully.
* Exports data to `Laptops.xlsx`.

### IMDb Movie Scraper
* Navigates IMDb's advanced search interface.
* Filters movies by release date (2010-01 to 2025-05).
* Dynamically loads up to 2250 movie entries by interacting with "Load More" buttons.
* Extracts comprehensive details for each movie: title, year, duration, IMDb rating, genres, director, main stars, and Metascore.
* Handles potential missing data on individual movie pages.
* Exports data to `movies.xlsx`.

## Technologies Used

* **Python 3.x**
* **Requests:** For making HTTP requests (eBay).
* **BeautifulSoup4:** For parsing HTML (eBay).
* **Selenium:** For browser automation and handling dynamic content (IMDb).
* **Pandas:** For data manipulation and exporting to Excel.
* **ChromeDriver (or other WebDriver):** Required for Selenium to control a Chrome browser instance.

## Prerequisites

Before running these scripts, ensure you have:

* **Python 3.x** installed.
* **pip** (Python package installer).
* **Google Chrome browser** installed.
* **ChromeDriver:** Download the appropriate version for your Chrome browser from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads). Place the `chromedriver` executable in a directory that is in your system's PATH, or update the `webdriver.Chrome()` call in `imdb_movies_scraper.py` with the full path to your driver (e.g., `webdriver.Chrome(executable_path='/path/to/chromedriver', options=options)`).

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your_username/your_project_name.git](https://github.com/your_username/your_project_name.git)
    cd your_project_name
    ```
    *(Remember to replace `your_username/your_project_name` with your actual GitHub path)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install beautifulsoup4 requests selenium pandas
    ```

## Usage

### eBay Laptop Scraper

This script (`ebay_laptops_scraper.py`) will automatically start scraping laptop data from eBay and save it to an Excel file.

To run the eBay scraper:

```bash
python ebay_laptops_scraper.py
