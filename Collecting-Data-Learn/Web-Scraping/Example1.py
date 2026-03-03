import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com/"
response = requests.get(url)

print(response.status_code)

# Beginner Scrapping
soup = BeautifulSoup(response.text,"html.parser")

quotes = soup.find_all("div",class_="quote")

for quote in quotes:
    text = quote.find("span",class_="text").text
    author = quote.find("small",class_="author").text
    if text and author:
        print(text ,"-",author)

tags = soup.find_all("div",class_="tags")

for tag in tags:
    link_list = tag.find_all("a",class_="tag")
    
    for tags in link_list:
        print("Tags : ",tag.text)

# professional Way Scrapping
def quote_text():
    quotes = soup.find_all("div",class_="quote")
    
    for quote in quotes:
        text = quote.find("span",class_="text").text
        author = quote.find("small",class_="author").text

        tags = quote.find_all("a",class_="tag")
        tag_list = [tag.text for tag in tags]

        print("\nQuote: ",text)
        print("\nAuthor: ",author)
        print("\nTags: ",tag_list)

quote_text()

# Convert scrap data into DataFrame
def Quote_DataFrame():
    quotes = soup.find_all("div",class_="quote")
    data = []
    for quote in quotes:
        text = quote.find("span",class_="text")
        author = quote.find("small",class_="author")
        tags = quote.find_all("a",class_="tag")

        text = text.text if text else None
        author = author.text if author else None
        tags = ", ".join([tag.text for tag in tags])if tags else None

        data.append([text,author,tags])

    df = pd.DataFrame(data=data,columns=["Quote","Author","Tags"])

    print(df)


Quote_DataFrame()



