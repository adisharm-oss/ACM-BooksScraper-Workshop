
# ACM @ UMD — From Website to Dataset  
## Books Web Scraping Workshop (60-Minute Guided Build)

Welcome to the ACM Web Scraping Workshop!

This README is intentionally detailed so students can follow along step-by-step without confusion.

---

# 0. Workshop Overview

## 0.1 What You Will Learn

By the end of this workshop, you will know how to:

• Send HTTP requests using Python  
• Parse HTML using BeautifulSoup  
• Extract structured data (Title + Price)  
• Crawl multiple pages (pagination)  
• Save results into a CSV dataset  
• Apply basic ethical scraping practices  

---

# 1. Setup Instructions

## 1.1 Install Python (Windows)

1. Go to: https://www.python.org/downloads/
2. Download latest version.
3. IMPORTANT: Check **"Add Python to PATH"** during installation.
4. After installing, open Command Prompt and run:

```
python --version
pip --version
```

If `python` does not work, try:

```
py --version
py -m pip --version
```

---

## 1.2 Install Python (macOS)

1. Download Python from https://www.python.org/downloads/
2. Install package.
3. Open Terminal and run:

```
python3 --version
pip3 --version
```

---

## 1.3 Install VS Code (Recommended)

Download from: https://code.visualstudio.com/

---

# 2. Create a Virtual Environment

Windows:
```
python -m venv .venv
.venv\Scripts\activate
```

macOS:
```
python3 -m venv .venv
source .venv/bin/activate
```

You should now see (.venv) in your terminal.

---

# 3. Install Required Libraries

From project root:

```
pip install -r requirements.txt
```

Verify:

```
python -c "import requests, bs4, pandas; print('Ready!')"
```

---

# 4. Live Coding Walkthrough

Create:

starter_code/scraper.py

---

## Step 1 — Make a Request

```python
import requests

url = "https://books.toscrape.com/"
response = requests.get(url)

print("Status code:", response.status_code)
print(response.text[:200])
```

Expected:
Status code 200 + HTML preview.

---

## Step 2 — Parse HTML

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text.strip())
```

---

## Step 3 — Find Books

```python
books = soup.find_all("article", class_="product_pod")
print("Books found:", len(books))
```

---

## Step 4 — Extract Title + Price

```python
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    print(title, "|", price)
```

---

## Step 5 — Store Results

```python
results = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    results.append({"Title": title, "Price": price})

print(results[:3])
```

---

## Step 6 — Pagination (First 5 Pages)

```python
import time

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

all_results = []

for page in range(1, 6):
    print("Scraping page", page)
    url = BASE_URL.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        all_results.append({"Title": title, "Price": price})

    time.sleep(1)

print("Total books:", len(all_results))
```

---

## Step 7 — Save to CSV

Create folder:

data/

Then:

```python
import pandas as pd

df = pd.DataFrame(all_results)
df.to_csv("data/books.csv", index=False)

print("Saved CSV.")
```

---

# Ethical Scraping Reminder

• Respect robots.txt  
• Use rate limiting  
• Avoid scraping personal data  
• Never overload servers  

---

# Final Run Command

From project root:

```
python starter_code/scraper.py
```

---

ACM @ UMD Web Scraping Workshop  
Build responsibly. Automate ethically. 🚀
