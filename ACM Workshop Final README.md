
# ACM @ UMD — From Website to Dataset
## Web Scraping Workshop (Guided Build Edition)

Welcome to the official ACM @ UMD Web Scraping Workshop repository.

This workshop walks you step-by-step from a scaffolded starter file (`scraper.py`) 
to a fully modular production-style scraper (`solution_scraper.py`).

This README is intentionally detailed and numbered (1.1, 2.1, etc.) 
so you can follow along live and easily jump to sections if you get lost.

------------------------------------------------------------
0. ABOUT ACM @ UMD
------------------------------------------------------------

0.1 Who We Are

ACM @ UMD is one of the largest technical student organizations on campus.

We run:
• Technical workshops
• Interview prep sessions
• Project-based learning
• Industry networking events
• Social impact tech initiatives

If you enjoyed this workshop, come to more ACM events.

------------------------------------------------------------
1. WORKSHOP OVERVIEW
------------------------------------------------------------

1.1 What You Will Learn

By the end of this workshop, you will know how to:

• Send HTTP requests using Python
• Parse raw HTML using BeautifulSoup
• Extract structured data from nested tags
• Loop through multiple pages (pagination)
• Build modular functions
• Save results into a CSV dataset
• Apply basic ethical scraping practices

------------------------------------------------------------
2. PROJECT STRUCTURE
------------------------------------------------------------

2.1 Files in This Repository

• starter_code/scraper.py → Scaffolded version (we build from this)
• solution_code/solution_scraper.py → Completed reference solution
• requirements.txt → Required Python libraries

------------------------------------------------------------
3. ENVIRONMENT SETUP
------------------------------------------------------------

3.1 Install Python

Download from:
https://www.python.org/downloads/

Windows:
✓ Check “Add Python to PATH”

Verify:
python --version
pip --version

Mac:
python3 --version
pip3 --version

------------------------------------------------------------

3.2 Create a Virtual Environment

Windows:
python -m venv .venv
.venv\Scripts\activate

Mac:
python3 -m venv .venv
source .venv/bin/activate

You should now see (.venv) in your terminal.

------------------------------------------------------------

3.3 Install Dependencies

pip install -r requirements.txt

Verify installation:
python -c "import requests, bs4, pandas; print('Ready!')"

------------------------------------------------------------
4. BUILDING THE SCRAPER — STEP BY STEP
------------------------------------------------------------

4.1 STEP 1 — Imports

We import:

• requests → sends HTTP requests
• BeautifulSoup → parses HTML
• pandas → creates CSV datasets
• time → rate limiting

Why?
Each tool handles one responsibility.

------------------------------------------------------------

4.2 STEP 2 — Base URL

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

The {} allows dynamic page number insertion using .format(page).

------------------------------------------------------------

4.3 STEP 3 — fetch_page()

Purpose:
Encapsulates request logic.

Starter version:
• Sends request
• Checks status code
• Returns BeautifulSoup object

Solution improvements:
• Adds timeout=10
• Adds warning messages

Why modularize?
Reusable, cleaner, easier debugging.

------------------------------------------------------------

4.4 STEP 4 — extract_books()

Purpose:
Extract structured data from parsed HTML.

Steps:
1. Find all <article class="product_pod">
2. Loop through each book
3. Extract title using book.h3.a["title"]
4. Extract price using class "price_color"

Solution adds:
• try/except for defensive coding

Why?
Real websites break. Robust code handles that.

------------------------------------------------------------

4.5 STEP 5 — Pagination

for page in range(1, 6):

Why?
Scales automation from 1 page to multiple pages.

BASE_URL.format(page) generates:
page-1.html
page-2.html
etc.

------------------------------------------------------------

4.6 STEP 6 — Rate Limiting

time.sleep(1)

Why?
• Prevents overwhelming servers
• Demonstrates ethical scraping
• Professional practice

------------------------------------------------------------

4.7 STEP 7 — Aggregating Data

all_books.extend(page_books)

Why?
Each page returns a list.
We combine them into one master dataset.

------------------------------------------------------------

4.8 STEP 8 — Save to CSV

df = pd.DataFrame(all_books)
df.to_csv("books.csv", index=False)

Why?
Transforms Python dictionaries into a structured dataset usable in Excel or Sheets.

Starter may use:
data/books.csv

Solution uses:
books.csv

------------------------------------------------------------
5. ETHICAL SCRAPING PRINCIPLES
------------------------------------------------------------

5.1 Always Check robots.txt
https://books.toscrape.com/robots.txt

5.2 Use Rate Limiting

5.3 Avoid scraping:
• Login pages
• Personal data
• Private dashboards

------------------------------------------------------------
6. COMMON ERRORS
------------------------------------------------------------

6.1 ModuleNotFoundError
Virtual environment not active.

6.2 Cannot save file into non-existent directory
Folder path in to_csv() does not exist.

6.3 Status code not 200
Check URL formatting.

------------------------------------------------------------
7. EXTENSIONS
------------------------------------------------------------

Try adding:
• Book rating extraction
• Availability extraction
• Scrape all 50 pages
• Export to JSON
• Perform price analysis

------------------------------------------------------------
8. RUN COMMANDS
------------------------------------------------------------

Starter:
python starter_code/scraper.py

Solution:
python solution_code/solution_scraper.py

------------------------------------------------------------
9. WHAT YOU BUILT
------------------------------------------------------------

You:
• Turned raw HTML into structured data
• Built modular scraping functions
• Implemented pagination
• Created a CSV dataset
• Practiced ethical automation

This is real-world automation engineering.

------------------------------------------------------------

ACM @ UMD
Build responsibly. Automate ethically. 🚀
