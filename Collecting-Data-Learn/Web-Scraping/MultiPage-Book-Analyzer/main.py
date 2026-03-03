from bs4 import BeautifulSoup
import requests
import pandas as pd 
import matplotlib.pyplot as plt 
from urllib.parse import urljoin

page = []
data = []
def collect_data():
    headers = {"User-Agent":"Mozilla/5.0"}
    base_url = "https://books.toscrape.com/"
    curnt_url = base_url
    print(curnt_url)
    
    while True:
        response = requests.get(curnt_url,headers=headers)
        if response.status_code == 200:
            print("API Connected Successfully !")

            soup = BeautifulSoup(response.text,"html.parser")

            books = soup.find_all("article", class_="product_pod")
            print("Books Count : ",len(books))

            for book in books:
                book_tag = book.find('h3').find('a')
                book_name = book_tag.text
                book_link = book_tag['href']

                price = book.find("p", class_="price_color").text
                availability = book.find("p", class_="instock availability").get_text(strip=True)
                if book_link:
                    book_url = urljoin(book_link,'index.html')


                data.append([book_name, book_link, price, availability])

            next_btn = soup.find("li",class_="next")
            crnt_page = 0
            if next_btn:
                nextpage = next_btn.find('a')['href']
                curnt_url = urljoin(curnt_url,nextpage)
                print(f"Current Page : {crnt_page}")
                crnt_page += 1
            else:
                print("There is No Pages")
                break



        else:
            print("There is problem in Connection !")

    
collect_data()

def convert_dataframe():
    df = pd.DataFrame(data=data,columns=["Book Name","Link","Price","Availability"])
    df.to_csv("Collecting-Data-Learn/Web-Scraping/MultiPage-Book-Analyzer/Book-Data.csv",mode='w',index=False,encoding="utf-8")
    print(df)
convert_dataframe()