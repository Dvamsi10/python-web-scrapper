import requests
from bs4 import BeautifulSoup
import csv

# 1. Fetch the Webpage Content
# The URL of the site we want to scrape.
URL = "http://quotes.toscrape.com/tag/life/"

# Send an HTTP GET request to the URL.
# The 'headers' help mimic a real browser visit.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
try:
    response = requests.get(URL, headers=headers)
    # Raise an exception if the request was unsuccessful (e.g., 404 Not Found).
    response.raise_for_status() 
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

# 2. Parse the HTML with BeautifulSoup
# Create a BeautifulSoup object to parse the page's content.
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Find and Extract the Data
# The website structure uses a 'div' with the class 'quote' for each quote block.
# We find all these blocks first.
quote_blocks = soup.find_all('div', class_='quote')

# Prepare a list to hold all our scraped data.
scraped_quotes = []

# Loop through each quote block to find the quote text and the author's name.
for quote_block in quote_blocks:
    # The quote text is inside a 'span' with the class 'text'.
    text_element = quote_block.find('span', class_='text')
    
    # The author's name is inside a 'small' tag with the class 'author'.
    author_element = quote_block.find('small', class_='author')

    # We check if both elements were found before trying to access their text.
    if text_element and author_element:
        # Get the text content and remove the surrounding quotation marks from the quote.
        quote_text = text_element.get_text(strip=True).strip('“”') 
        author_name = author_element.get_text(strip=True)
        
        # Add the scraped data as a dictionary to our list.
        scraped_quotes.append({'quote': quote_text, 'author': author_name})

# 4. Save the Data to a CSV File
# Define the name of the output file.
csv_file_name = 'quotes.csv'

# Open the CSV file in 'write' mode. 'newline=""' prevents extra blank rows.
try:
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as file:
        # Define the column headers for our CSV.
        fieldnames = ['quote', 'author']
        
        # Create a CSV DictWriter object.
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write the header row.
        writer.writeheader()
        
        # Write all the scraped quotes to the file.
        writer.writerows(scraped_quotes)
        
    print(f"✅ Success! Scraped {len(scraped_quotes)} quotes and saved them to '{csv_file_name}'")

except IOError as e:
    print(f"Error writing to file: {e}")
