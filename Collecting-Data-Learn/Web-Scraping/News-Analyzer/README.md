# 📰 News Headline Analyzer (Web Scraping + Data Analysis Project)

## 🚀 Project Overview

The **News Headline Analyzer** is a complete web scraping and data analysis project built using:

* **Python**
* **BeautifulSoup**
* **Requests**
* **Pandas**
* **Matplotlib**

This project scrapes live news headlines from Hacker News, processes the data, performs analysis, and generates visualizations to extract meaningful insights.

It demonstrates real-world skills in:

* Web Scraping
* Data Cleaning
* Feature Engineering
* Data Analysis
* Data Visualization

---

## 🎯 Project Objectives

✔ Scrape latest news articles
✔ Extract:

* Title
* Link
* Score (Points)

✔ Clean and preprocess data
✔ Perform statistical analysis
✔ Generate visual insights
✔ Save processed data as CSV
✔ Save visual graphs as images

---

---

## 🔍 Data Collection

Source:

```
https://news.ycombinator.com/
```

Extracted fields:

| Column | Description              |
| ------ | ------------------------ |
| Title  | Article headline         |
| Link   | Article URL              |
| Score  | Number of points (votes) |

Headers are used in requests to ensure proper data retrieval.

---

## 🧹 Data Cleaning

✔ Converted score text ("123 points") → integer
✔ Handled missing scores (replaced with 0)
✔ Removed duplicates
✔ Created new feature: **Title Length**

```python
df["Title Length"] = df["Title"].apply(len)
```

---

## 📊 Data Analysis

The analyzer function calculates:

🔥 Highest voted article
📉 Lowest voted article
📈 Top 5 trending articles
📊 Average score

Example output:

```
Highest Voted : Example Title, Score : 542
Lowest Voted : Example Title, Score : 3
Average Score : 127
```

---

## 📈 Visualizations

### 1️⃣ Top 10 Articles by Points

* Horizontal bar chart
* Saved as: `Top-10-news.png`

### 2️⃣ Distribution of Article Popularity

* Histogram
* Shows how article scores are distributed
* Saved as: `Score-distribution.png`

### 3️⃣ Title Length vs Score

* Scatter plot
* Shows relationship between headline length and popularity
* Saved as: `Title-length-vs-score.png`

---

## 🧠 Key Insights

* Most articles receive moderate to low scores.
* A small percentage of articles gain very high engagement.
* Title length shows weak or no strong correlation with score (based on correlation analysis).

---

## 🛠 Technologies Used

* Python 
* Requests
* BeautifulSoup4
* Pandas
* Matplotlib

---
## 📌 Future Improvements

* Add pagination (scrape multiple pages)
* Add sentiment analysis (NLP)
* Build interactive dashboard using Streamlit
* Store data in database
* Automate scheduled scraping

---

## 📖 Learning Outcomes

This project strengthens understanding of:

* HTML structure inspection
* Handling nested elements
* Managing missing data
* Feature engineering
* Exploratory Data Analysis (EDA)
* Visualization best practices

---

## 👨‍💻 Developer

**Herambha Karthikeya Guptha**

---

⭐ Feel free to explore, fork, and improve this project.
