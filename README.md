# RigPix Icom Radio Data Scraper

This Python script is a web scraping tool that extracts information about Icom radios from the [RigPix](http://www.rigpix.com/icom/icomselect.htm) website. It parses the HTML content of the webpage, retrieves data from specific tables, and organizes it into a dictionary for further analysis.

## Prerequisites

Before you begin, make sure you have the following:

- Python installed on your system.
- Required Python libraries, including `pandas`, `requests`, and `BeautifulSoup (bs4)`. You can install them using the following command:

   ```bash
   pip install pandas requests beautifulsoup4
   ```

## Usage

1. Clone this repository or download the script.

2. Open the script and make the following adjustments as needed:

   - Set the `url` variable to the URL of the RigPix webpage containing Icom radio data.

3. Run the script using the following command:

   ```bash
   python rigpix_icom_scraper.py
   ```

4. The script will fetch the HTML content of the specified webpage and parse it to extract data from tables.

5. It retrieves information about Icom radios and organizes it into a dictionary, where each key represents a category (e.g., "HF Transceivers," "VHF/UHF Transceivers") and the corresponding value is a DataFrame containing the radio models and details within that category.

6. The extracted data is printed to the console as a dictionary.

## Example

Here's an example of what the script's output might look like (simplified for brevity):

```python
{
    'HF Transceivers':              ...,
    'VHF/UHF Transceivers':         ...,
    'Professional Transceivers':    ...,
    'Receivers':                    ...,
    'Accessories':                  ...,
    ...
}
```

Each category contains a DataFrame with radio model details, such as model name, bands, and modes.

## Note

- The script is tailored to extract data from the specific RigPix webpage provided in the `url` variable. If you want to scrape data from a different webpage or website, you may need to adapt the script to the HTML structure of that page.

- Depending on your use case, you can customize the script to save the extracted data to a file, perform further data analysis, or integrate it into other projects as necessary.

Feel free to explore and customize the script to meet your specific requirements or integrate it into other projects as necessary.
