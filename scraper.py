"""
ACM @ UMD — Web Scraping Workshop
Starter Script: Books to Scrape

This file is intentionally built in stages.
We will progressively add functionality during the workshop.
"""

# ================================
# STEP 1 — IMPORT LIBRARIES
# ================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# ================================
# STEP 2 — BASE URL SETUP
# ================================

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

# ================================
# STEP 3 — SCRAPE FIRST 5 PAGES
# ================================

all_results = []

for page in range(1, 6):
    print(f"Scraping page {page}...")
    
    url = BASE_URL.format(page)
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch page {page}")
        continue
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        try:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            
            all_results.append({
                "Title": title,
                "Price": price
            })
        except Exception as e:
            print("Error parsing a book:", e)
    
    # Basic rate limiting
    time.sleep(1)

# ================================
# STEP 4 — SAVE TO CSV
# ================================

df = pd.DataFrame(all_results)
df.to_csv("data/books.csv", index=False)

print("\nScraping complete!")
print(f"Saved {len(all_results)} books to data/books.csv")
