import requests
from bs4 import BeautifulSoup
import csv

# Make a request to the website
url = "https://www.bjjheroes.com/a-z-bjj-fighters-list"
response = requests.get(url)

# Create a Beautiful Soup object
soup = BeautifulSoup(response.text, "html.parser")

# Find the table with the specified ID
table = soup.find("tbody", {"class":"row-hover"})

with open("data_new_sep.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["First Name", "Last Name", "Nickname", "Team", "Link"])
    # Iterate over each row in the table
    for row in table.find_all("tr"):
        # Find all the td elements in the row
        tds = row.find_all("td")

        # Extract the text from each td element
        data = [td.get_text(strip=True) for td in tds]
        data_str = '|'.join(data)
        # Find the first anchor tag in the row
        anchor = row.find("a")
        # Extract the href attribute value
        href = anchor["href"]
        href_response = requests.get("https://www.bjjheroes.com"+href)
        # Create a Beautiful Soup object for the href URL
        href_soup = BeautifulSoup(href_response.text, "html.parser")

        # Find the table with the specified class
        href_table = href_soup.find("tbody")
        #print(data, href_table)
        if href_table:
            #print(href_table)
            # Extract the data from the table
            for href_row in href_table.find_all("tr"):
                # Find all the td elements in the row
                href_tds = href_row.find_all("td")
                #print(href_tds, "href_tds")
                # Extract the text from each td element
                href_data = [td.get_text(strip=True) for td in href_tds]
                #print(href_data, "href_data")
                # Write the href and data to the CSV file
                href_data_str = '|'.join(href_data)
                #print(href_data_str)
                writer.writerow([href ,data_str, href_data_str])
        else:
            writer.writerow([href, data, None])
        # Flush the file buffer to ensure data is written to disk
        file.flush()