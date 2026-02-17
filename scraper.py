"""
ACM @ UMD — Web Scraping Workshop
Starter Scraper

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
    # Format URL (already done)
    url = BASE_URL.format(page_number)

    # TODO:
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
# STEP 5 — MAIN SCRAPER LOGIC
# ======================================

def main():

    all_books = []

    # Implement the loop

        # TODO (YOU IMPLEMENT):
        # Add ethical rate limiting here

    if not all_books:
        #Implement what happens if no books are scraped.

    df = pd.DataFrame(all_books)

    # TODO:
    # Save DataFrame to CSV using OUTPUT_PATH

    print("\nScraping complete!")
    print(f"Total books scraped: {len(all_books)}")
    print(f"Data saved to: {OUTPUT_PATH}")


# ======================================
# RUN SCRIPT
# ======================================

if __name__ == "__main__":
    main()
