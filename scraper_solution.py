"""
ACM @ UMD — Web Scraping Workshop
Solution Script: Books to Scrape

This version includes:
• Modular functions
• Basic error handling
• Pagination (first 5 pages)
• CSV export
• Rate limiting
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
OUTPUT_PATH = "data/books.csv"


# ======================================
# Function: Fetch and parse a page
# ======================================
def fetch_page(page_number):
    url = BASE_URL.format(page_number)
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print(f"Warning: Failed to fetch page {page_number}")
        return None

    return BeautifulSoup(response.text, "html.parser")


# ======================================
# Function: Extract book data from page
# ======================================
def extract_books(soup):
    books_data = []
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        try:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text

            books_data.append({
                "Title": title,
                "Price": price
            })
        except Exception as e:
            print("Error extracting book:", e)

    return books_data


# ======================================
# Main Scraper Logic
# ======================================
def main():
    all_books = []

    for page in range(1, 6):
        print(f"Scraping page {page}...")

        soup = fetch_page(page)
        if soup is None:
            continue

        page_books = extract_books(soup)
        all_books.extend(page_books)

        # Ethical rate limiting
        time.sleep(1)

    if not all_books:
        print("No books scraped. Exiting.")
        return

    df = pd.DataFrame(all_books)
    df.to_csv(OUTPUT_PATH, index=False)

    print("\nScraping complete!")
    print(f"Total books scraped: {len(all_books)}")
    print(f"Data saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
