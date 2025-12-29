import requests
from bs4 import BeautifulSoup
import csv  # New library for handling CSV files

# 1. Define URL and Headers
url = "https://www.commoditymarketlive.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", {"id": "stateprices"})
rows = table.find_all("tr")
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(
        [
            "Commodity",
            "1KG Price",
            "1Q Price",
            " Max Price",
            "Min Price",
            "Prev Price",
            " Arrival",
        ]
    )

    for row in rows:
        cells = row.find_all("td")

        data = []
        for cell in cells:
            # PRIORITY 1: extract hidden attribute
            if cell.has_attr("data-sort-value"):
                data.append(cell["data-sort-value"])
            else:
                data.append(cell.get_text(strip=True))

        writer.writerow(data)

print("✔ Saved to output.csv")
