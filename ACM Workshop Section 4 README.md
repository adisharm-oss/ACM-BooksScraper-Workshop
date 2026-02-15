
------------------------------------------------------------
4. BUILDING THE SCRAPER — STEP BY STEP (COPY/PASTE FRIENDLY)
------------------------------------------------------------

This section is designed so you can follow the live workshop even if you fall behind.

Rules for success:
• After every step, RUN the file and confirm it works before moving on.
• Copy the code blocks exactly.
• Save the file after every edit.

File we are editing:
• starter_code/scraper.py

Goal:
• Build up `scraper.py` until it behaves like `solution_scraper.py`.

------------------------------------------------------------
4.0 STARTING POINT (CHECK YOUR FILE MATCHES)
------------------------------------------------------------

Before we begin: your `starter_code/scraper.py` should already look like the scaffold version
(contains BASE_URL, fetch_page(), extract_books(), main(), and the __main__ block).

If you are unsure, re-download the starter file from the repo.

------------------------------------------------------------
4.1 STEP 1 — VERIFY IMPORTS
------------------------------------------------------------

Make sure these imports exist at the top of your file:

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
```

RUN CHECKPOINT:
python starter_code/scraper.py

If you see ModuleNotFoundError:
→ Run: pip install -r requirements.txt

------------------------------------------------------------
4.2 STEP 2 — VERIFY BASE URL
------------------------------------------------------------

Make sure this exists:

```python
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
```

The {} allows dynamic page insertion using .format(page_number).

------------------------------------------------------------
4.3 STEP 3 — REPLACE fetch_page()
------------------------------------------------------------

Replace your ENTIRE fetch_page() function with:

```python
def fetch_page(page_number):
    url = BASE_URL.format(page_number)
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print(f"Warning: Failed to fetch page {page_number}")
        return None

    return BeautifulSoup(response.text, "html.parser")
```

RUN CHECKPOINT:
Temporarily test inside main():
print(fetch_page(1).title.text)

Then remove the test line.

------------------------------------------------------------
4.4 STEP 4 — REPLACE extract_books()
------------------------------------------------------------

Replace your ENTIRE extract_books() function with:

```python
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
```

RUN CHECKPOINT:
File should execute without crashing.

------------------------------------------------------------
4.5 STEP 5 — REPLACE main()
------------------------------------------------------------

Replace your ENTIRE main() function with:

```python
def main():
    all_books = []

    for page in range(1, 6):
        print(f"Scraping page {page}...")

        soup = fetch_page(page)
        if soup is None:
            continue

        page_books = extract_books(soup)
        all_books.extend(page_books)

        time.sleep(1)

    if not all_books:
        print("No books scraped. Exiting.")
        return

    df = pd.DataFrame(all_books)
    df.to_csv("books.csv", index=False)

    print("\nScraping complete!")
    print(f"Total books scraped: {len(all_books)}")
    print("Data saved to: books.csv")
```

RUN CHECKPOINT:
python starter_code/scraper.py

Expected:
• Scrapes 5 pages
• Creates books.csv
• Prints total books scraped

------------------------------------------------------------
4.6 STEP 6 — ADD OUTPUT_PATH CONSTANT (CLEANER DESIGN)
------------------------------------------------------------

Add near the top of your file:

```python
OUTPUT_PATH = "books.csv"
```

Replace:
df.to_csv("books.csv", index=False)

With:
df.to_csv(OUTPUT_PATH, index=False)

Replace final print line with:
print(f"Data saved to: {OUTPUT_PATH}")

RUN CHECKPOINT:
python starter_code/scraper.py

------------------------------------------------------------
4.7 FINAL VERIFICATION
------------------------------------------------------------

Your scraper should now:

• Scrape pages 1–5
• Extract Title and Price
• Sleep 1 second between pages
• Save to books.csv
• Print total books scraped

You now have a fully working scraper.

------------------------------------------------------------
5. ETHICAL SCRAPING PRINCIPLES
------------------------------------------------------------

5.1 Always check robots.txt when scraping real sites.

5.2 Use rate limiting (time.sleep).

5.3 Never scrape:
• Login-required pages
• Personal data
• Sites that disallow bots

------------------------------------------------------------
6. EXTENSIONS (OPTIONAL)
------------------------------------------------------------

6.1 Add Rating Extraction:
Look for:
<p class="star-rating Three">

6.2 Add Availability Extraction:
Look for:
<p class="instock availability">

6.3 Scrape More Pages:
Change range(1, 6) to range(1, 11)

6.4 Export JSON:
df.to_json("books.json", orient="records", indent=2)

------------------------------------------------------------
7. RUN COMMANDS
------------------------------------------------------------

Starter:
python starter_code/scraper.py

Solution:
python solution_code/solution_scraper.py

------------------------------------------------------------
8. WHAT YOU BUILT
------------------------------------------------------------

You:
• Turned raw HTML into structured data
• Built modular scraping functions
• Implemented pagination
• Created a CSV dataset
• Practiced ethical automation

ACM @ UMD — Build responsibly. Automate ethically. 🚀
