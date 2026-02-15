"""
ACM @ UMD — Web Scraping Workshop
Starter Scraper (Scaffold Version)

This file is intentionally incomplete.
We will implement the missing parts together.
"""

# ======================================
# STEP 1 — IMPORT LIBRARIES
# ======================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# ======================================
# STEP 2 — BASE URL
# ======================================

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"


# ======================================
# STEP 3 — FETCH A PAGE
# ======================================

def fetch_page(page_number):
    """
    Sends a request to a specific page number.
    Returns BeautifulSoup object.
    """
    url = BASE_URL.format(page_number)

    # TODO:
    # 1. Send request using requests.get()
    # 2. Check status code
    # 3. Return BeautifulSoup object

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch page {page_number}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    return soup


# ======================================
# STEP 4 — EXTRACT BOOK DATA
# ======================================

def extract_books(soup):
    """
    Takes a BeautifulSoup object.
    Returns a list of dictionaries.
    """
    books_data = []

    # TODO:
    # 1. Find all book containers
    # 2. Loop through each book
    # 3. Extract title
    # 4. Extract price
    # 5. Append to books_data list

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text

        books_data.append({
            "Title": title,
            "Price": price
        })

    return books_data


# ======================================
# STEP 5 — MAIN SCRAPER LOOP
# ======================================

def main():
    all_books = []

    # TODO:
    # Loop through first 5 pages

    for page in range(1, 6):
        print(f"Scraping page {page}...")

        soup = fetch_page(page)

        if soup is None:
            continue

        page_books = extract_books(soup)
        all_books.extend(page_books)

        # Ethical scraping — rate limiting
        time.sleep(1)

    # ======================================
    # STEP 6 — SAVE TO CSV
    # ======================================

    if not all_books:
        print("No books scraped.")
        return

    df = pd.DataFrame(all_books)

    # TODO:
    # Make sure data folder exists
    # Save CSV file

    df.to_csv("data/books.csv", index=False)

    print("\nScraping complete!")
    print(f"Total books scraped: {len(all_books)}")


# ======================================
# RUN SCRIPT
# ======================================

if __name__ == "__main__":
    main()
