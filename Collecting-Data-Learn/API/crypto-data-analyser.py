import requests 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from datetime import datetime

url = "https://api.coingecko.com/api/v3/coins/markets"

def Collect_Data():
    params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
    }
    response = requests.get(url=url,params=params)
    if response.status_code == 200:
        print("Connected Successfully")
    data = response.json()
    df = pd.json_normalize(data)
    df = df[["name","current_price","market_cap","total_volume","price_change_percentage_24h","high_24h","low_24h"]]
    file_name = "Collecting-Data-Learn/API/crypto_data.csv" 
    df.to_csv(file_name,mode='a',index= False,encoding="utf-8")
#Collect_Data()

def analyze_crypto(df):
    highest_gainer = df.loc[df["24 Change %"].idxmax()]

    lowest_loser = df.loc[df["24 Change %"].idxmin()]

    highest_market_cap = df.loc[df["Market Cap"].idxmax()]

    most_volatile = df.loc[df["Volatility"].idxmax()]

    print("\n Hightest 24h Gainer:")
    print(highest_gainer["Name"],highest_gainer["24 Change %"])

    print("\n Biggest Loser:")
    print(lowest_loser["Name"],lowest_loser["24 Change %"])

    print("\n Highest Market Cap Coin:")
    print(highest_market_cap["Name"],highest_market_cap["Market Cap"])

    print("\n Most Volatile Coin:")
    print(most_volatile["Name"],most_volatile["Volatility"])


def clean_data():
    df = pd.read_csv("Collecting-Data-Learn/API/crypto_data.csv")
    df.rename(columns={
        "name":"Name",
        "current_price":"Current Price",
        "market_cap":"Market Cap",
        "price_change_percentage_24h":"24 Change %",
        "high_24h":"High 24h",
        "low_24h":"Low 24h",
        "total_volume":"Total Volume"
    },inplace=True)
    
    df["24 Change %"] = df["24 Change %"].fillna(df["24 Change %"].mean())
    df["High 24h"] = df["High 24h"].fillna(df["High 24h"].mean())
    df["Low 24h"] = df["Low 24h"].fillna(df["Low 24h"].mean())

    df["Time Stamp"] = datetime.utcnow()
    df["Volatility"] = df["High 24h"] - df["Low 24h"]

    df.to_csv("Collecting-Data-Learn/API/crypto_data.csv",mode='w',index=False,encoding="utf-8")
    print("Cleaned Data:\n")
    print(df)

    analyze_crypto(df)
clean_data()

def visualization():
    df = pd.read_csv("Collecting-Data-Learn/API/crypto_data.csv")

    # Bar Chart
    plt.bar(df["Name"],df["Market Cap"])
    plt.title("Market Cap Comaprison")
    plt.xlabel("Crypto Coin Name")
    plt.ylabel("Crypto Market Cap")
    plt.savefig("Collecting-Data-Learn/API/graph-images/market-cap.png")
    plt.show()

    # Scatter
    plt.scatter(df["Total Volume"],df["Current Price"])
    plt.title("Volume vs Price")
    plt.xlabel("Crypto Volume")
    plt.ylabel("Crypto Price")
    plt.savefig("Collecting-Data-Learn/API/graph-images/volume-vs-price.png")
    plt.show()

    # Line Plot 
    plt.plot(df["Current Price"],df["Name"],marker="o")
    plt.title("Price Range Of Crypto")
    plt.xlabel("Crypto Coin")
    plt.ylabel("Crypto Coin Price")
    plt.savefig("Collecting-Data-Learn/API/graph-images/crypto-price-range.png")
    plt.show()

    # hist
    plt.hist(df["High 24h"],bins=20)
    plt.title("Data Visualize Histogram")
    plt.xlabel("Crypto Coin")
    plt.ylabel("Crypto Coin High 24")
    plt.savefig("Collecting-Data-Learn/API/graph-images/hist-visualization.png")
    plt.show()
visualization()
