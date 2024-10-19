import pandas as pd
import requests
from bs4 import BeautifulSoup

def fetch_page_content(url: str) -> BeautifulSoup:
    """Fetches the content of a webpage and returns a BeautifulSoup object."""
    response = requests.get(url)
    response.raise_for_status()  # Ensure we raise an error for failed requests
    return BeautifulSoup(response.text, 'html.parser')

def extract_headers(soup: BeautifulSoup) -> list:
    """Extracts and returns a list of header texts (h3 tags) from the parsed HTML."""
    return [h.text for h in soup.find_all('h3')]

def extract_table_data(soup: BeautifulSoup, start_table_index: int = 3) -> dict:
    """Extracts tables from the webpage and maps them to the corresponding headers."""
    # Parse all tables in the webpage
    tables = pd.read_html(str(soup))
    
    # Extract headers for each table and map to respective header from the page
    headers = extract_headers(soup)
    return {headers[i]: table for i, table in enumerate(tables[start_table_index:])}

def main():
    url = "http://www.rigpix.com/icom/icomselect.htm"
    soup = fetch_page_content(url)
    data = extract_table_data(soup)
    
    # Display the extracted data
    for header, table in data.items():
        print(f"\nHeader: {header}")
        print(table)

if __name__ == "__main__":
    main()
