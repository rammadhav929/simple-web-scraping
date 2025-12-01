# simple-web-scraping

📌 Python Libraries Explanation
import requests


✔ Allows you to send HTTP requests to websites (GET, POST, etc.).
✔ Used to download a webpage’s HTML for scraping.

from bs4 import BeautifulSoup


✔ Comes from the BeautifulSoup4 library.
✔ Used to parse and extract data from HTML (e.g., tables, tags, text).

import csv  # New library for handling CSV files


✔ Python’s built-in module.
✔ Used to create and write data into CSV files (Excel-like format).
✔ Helpful to store scraped data for analysis.

The headers in web scraping are used to make your request look like a real browser. Many websites block bots or scripts, so sending headers makes the website think a real human is visiting.

✔ What these two lines do
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

🔹 1. response = requests.get(url, headers=headers)

This sends a request to the website (url).

The website replies with the HTML code.

That reply is stored in response.

headers help to pretend like a normal browser, so website doesn't block your request.

So this line downloads the HTML page.

🔹 2. soup = BeautifulSoup(response.text, "html.parser")

response.text contains the raw HTML code of that page.

BeautifulSoup takes that HTML and converts it into structured data, so we can search easily (find table, headings, links, etc.).

"html.parser" tells BeautifulSoup which parser to use.

This line parses the HTML for web scraping.
