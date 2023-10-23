import csv
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Define the URL
url = "https://en.wikipedia.org/wiki/Comparison_of_programming_languages"

# Create a function to scrape and write data to a CSV file
def scrape_and_write_to_csv(url, csv_filename):
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"class": "wikitable"})
    rows = table.findAll("tr")

    with open(csv_filename, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            cells = row.find_all(["td", "th"])
            writer.writerow([cell.get_text(strip=True) for cell in cells])

# Define the CSV filename
csv_filename = "language.csv"

# Scrape and write the data to the CSV file
scrape_and_write_to_csv(url, csv_filename)

# Read the CSV file using pandas
df = pd.read_csv(csv_filename)
print(df.head())
