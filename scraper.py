"""
ACM @ UMD — Web Scraping Workshop
Starter Scraper (Balanced Build Version)

This version contains structure and flow,
but core scraping logic must be implemented during the workshop.
"""

# ======================================
# STEP 1 — IMPORT LIBRARIES (Already Provided)
# ======================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# ======================================
# STEP 2 — BASE CONFIGURATION (Already Provided)
# ======================================

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
OUTPUT_PATH = "books.csv"


# ======================================
# STEP 3 — FETCH A PAGE
# ======================================

def fetch_page(page_number):
    """
    Sends a request to a specific page.
    Returns BeautifulSoup object or None.
    """

    # Format URL (already done)
    url = BASE_URL.format(page_number)

    # TODO (YOU IMPLEMENT):
    # 1. Send request using requests.get()
    # 2. Add timeout=10
    # 3. Check status code
    # 4. If not 200 → print warning + return None

    response = None  # <-- replace this

    # TODO: Add status code check here

    # TODO: Return BeautifulSoup(response.text, "html.parser")

    pass  # remove once implemented


# ======================================
# STEP 4 — EXTRACT BOOK DATA
# ======================================

def extract_books(soup):
    """
    Extracts Title and Price from a parsed page.
    Returns a list of dictionaries.
    """

    books_data = []

    # TODO (YOU IMPLEMENT):
    # 1. Find all <article class="product_pod">
    # 2. Loop through each book
    # 3. Extract:
    #       - title
    #       - price
    # 4. Append dictionary to books_data

    # HINT:
    # books = soup.find_all("article", class_="product_pod")

    return books_data


# ======================================
# STEP 5 — MAIN SCRAPER LOGIC (Mostly Built)
# ======================================

def main():

    all_books = []

    # Pagination loop already provided
    for page in range(1, 6):
        print(f"Scraping page {page}...")

        soup = fetch_page(page)

        if soup is None:
            continue

        page_books = extract_books(soup)
        all_books.extend(page_books)

        # TODO (YOU IMPLEMENT):
        # Add ethical rate limiting here

    if not all_books:
        print("No books scraped. Exiting.")
        return

    df = pd.DataFrame(all_books)

    # TODO (YOU IMPLEMENT):
    # Save DataFrame to CSV using OUTPUT_PATH

    print("\nScraping complete!")
    print(f"Total books scraped: {len(all_books)}")
    print(f"Data saved to: {OUTPUT_PATH}")


# ======================================
# RUN SCRIPT
# ======================================

if __name__ == "__main__":
    main()
