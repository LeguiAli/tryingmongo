import requests
from bs4 import BeautifulSoup
import csv

# Make a request to the website
url = "https://www.learn-japanese-adventure.com/japanese-schools.html"
response = requests.get(url)

# Create a Beautiful Soup object
soup = BeautifulSoup(response.text, "html.parser")

# Find the table with the specified ID
table = soup.find("table")

#print(table)

with open("vocab.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Num", "Kanji", "Hiragana/Katakana", "Romaji", "Meaning"])
    # Iterate over each row in the table
    for row in table.find_all("tr"):
        # Find all the td elements in the row
        tds = row.find_all("td")
        # Extract the text from each td element
        data = [td.get_text(strip=True) for td in tds]
        data_str = '|'.join(data)
        writer.writerow([data])