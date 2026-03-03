import pandas as pd 
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"

def Data_Scraping():
    data = []
    headers = {
        "User-Agent":"Mozilla/5.0"
    }
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")

    newses = soup.find_all("span",class_="titleline")
    news_score = soup.find_all("span",class_="score")

    print("News Titles :",len(newses))
    print("News Score : ",len(news_score))

    for i in range(len(newses)):
        a_tag = newses[i].find("a")
        title = a_tag.text 
        link = a_tag["href"]
        
        if i < len(news_score):
            score_text = news_score[i].text
            score = int(score_text.split()[0])
        else:
            score = 0
        data.append([title,link,score])

    return data

def Analyzer(df):
    higesh_score = df.loc[df["Score"].idxmax()]
    print(f"Higesht Voted : {higesh_score["Title"]}, Score : {higesh_score["Score"]}")

    lowest_score = df.loc[df["Score"].idxmin()]
    print(f"Lowest Voted : {lowest_score["Title"]}, Score : {lowest_score["Score"]}")

    average_score = df["Score"].mean()
    print(f"Average Of Score : ",int(average_score))


def Scrap_DataFrame():
    data = Data_Scraping()

    df = pd.DataFrame(data,columns=["Title","Link","Score"])
    print(df)
    df.to_csv("Collecting-Data-Learn/Web-Scraping/News-Analyzer/Scrap_Data.csv",index=False,encoding="utf-8")
    Analyzer(df)

Scrap_DataFrame()

def visualize():
    df =pd.read_csv("Collecting-Data-Learn/Web-Scraping/News-Analyzer/Scrap_Data.csv")

    top10 = df.sort_values(by="Score",ascending=False).head(10)

    plt.figure(figsize=(12,8))
    plt.barh(top10["Title"],top10["Score"])
    plt.title("Top 10 Newses")
    plt.xlabel("News Title")
    plt.ylabel("Score Of News")
    plt.gca().invert_yaxis()  # highest on top
    plt.tight_layout()
    plt.savefig("Collecting-Data-Learn/Web-Scraping/News-Analyzer/graph-images/Top-10-news.png")
    plt.show()

    plt.hist(df["Score"],bins=20)
    plt.title("News Distribution")
    plt.xlabel("Points")
    plt.savefig("Collecting-Data-Learn/Web-Scraping/News-Analyzer/graph-images/News-Distribution.png")
    plt.ylabel("Number Of Articles")
    plt.show()

    df["Title_length"] = df["Title"].apply(len)
    plt.scatter(df["Title_length"],df["Score"])
    plt.xlabel("Title length")
    plt.ylabel("Score")
    plt.title("Title Length vs Score")
    plt.savefig("Collecting-Data-Learn/Web-Scraping/News-Analyzer/graph-images/title-len-vs-score.png")
    plt.show()

visualize()

