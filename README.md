# python-web-scrapper
A simple Python web scraper that extracts quotes and authors from a website and saves them to a CSV file using requests and BeautifulSoup.



# Python Quote Scraper 🕸️

This is a simple yet powerful web scraping script created in Python. It's designed as a beginner-friendly project to demonstrate the fundamentals of fetching and parsing web data.

## What it Does

-   **Fetches** the HTML content from the website `http://quotes.toscrape.com/`.
-   **Parses** the HTML to find all the quotes and their corresponding authors.
-   **Saves** the extracted data neatly into a structured `quotes.csv` file.

## Technologies Used

-   **Python 3**
-   **Requests:** For making HTTP requests to the webpage.
-   **BeautifulSoup4:** For parsing HTML and extracting data.

## How to Run

1.  Clone or download the repository.
2.  Install the required libraries:
    ```bash
    pip install requests beautifulsoup4
    ```
3.  Run the script:
    ```bash
    python scraper.py
    ```
4.  A `quotes.csv` file will be generated in the same directory.
