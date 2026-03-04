# 📚 MultiPage Book Analyzer (Web Scraping Project)

## 🚀 Project Overview

This project is a web scraping application built using **Python, BeautifulSoup, Requests, and Pandas**.

It extracts book data from:

👉 https://books.toscrape.com/

The scraper collects data from:
- Multiple pages (pagination)
- Individual book detail pages
- Product information tables

Finally, it saves the collected data into a **CSV file** for analysis.

---

## 🛠 Technologies Used

- Python
- BeautifulSoup
- Requests
- Pandas
- urllib.parse
- Time module (for delay handling)

---

## 📂 Features

- ✅ Multi-page scraping  
- ✅ Pagination handling  
- ✅ Inner page data extraction  
- ✅ Table data extraction   
- ✅ CSV conversion  
- ✅ Timeout handling  
- ✅ User-Agent header implementation  

---

## 📊 Data Collected

For each book, the following details are extracted:

- Book Name  
- Book URL  
- Price (Main Page)  
- Availability (Main Page)  
- UPC  
- Product Type  
- Price (Excluding Tax)  
- Price (Including Tax)  
- Tax  
- Number of Reviews  

---

## ⚙️ How It Works

1. Connect to the main page.
2. Extract book links.
3. Visit each book's detail page.
4. Extract table data.
5. Store data in dictionary format.
6. Convert CSV.

---

## ▶️ How to Run

1. Install required libraries:

```bash
pip install requests beautifulsoup4 pandas
```

2. Run the script:

```bash
python main.py
```

3. Output file will be generated:

```
Book-Data.csv
```

---

## 📁 Project Structure

```
MultiPage-Book-Analyzer/
│
├── main.py
├── Book-Data.csv
└── README.md
```

---

## 🧠 Learning Outcomes

Through this project, I learned:

- Handling pagination in web scraping
- Extracting structured table data
- Managing relative and absolute URLs
- Handling timeout errors
- Converting CSV using Pandas
- Building structured datasets

---

## 👨‍💻 Developer

Developed by **Herambha Karthikeya Guptha**
