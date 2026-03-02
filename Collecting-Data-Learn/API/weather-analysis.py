import requests
import pandas as pd 
import matplotlib.pyplot as plt 
from datetime import datetime
import seaborn as sns 

Cities = ["vijayawada","ongole","tirupati","chirala","bapatla","uppugunduru","gunturu","bengaluru","visakhapatnam","chennai"]
print(f"I collect data from {len(Cities)} cities .... ")
API_KEY = "28529f3a8c4ae80afcc3fa1ae09856de"

def Collect_Data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url)
    if response.status_code != 200:
        print("The API not work try again..!")
    data = response.json()
    df = pd.json_normalize(data,record_path=["weather"],meta=['name',['main','humidity'],['main','pressure'],['wind','speed'],['main','temp']])
    df = df[["name","main.humidity","main.pressure","description","wind.speed","main.temp"]]
    df["Temp_Celsius"] = df["main.temp"] - 273.15
    df["Date-Time"] = datetime.utcnow()
    df.to_csv("Collecting-Data-Learn/API/all-colleting-data.csv",mode='a',index=False,header=False,encoding="utf-8")

"""for city in Cities:
    Collect_Data(city)
    print(f"Data Collected From {city}")
print("Data Collected Successfully !")"""    # if data file not have run this 
def clean_data():
    column_names=["City","Humidity","Pressure","Desription","Wind-Speed","Kelvin-Temp","Celsius-Temp","Date-Time"]
    df = pd.read_csv("Collecting-Data-Learn/API/all-colleting-data.csv",header=None,names=column_names)
   
    df["Humidity"] = df["Humidity"].astype(int)
    df["Pressure"] = df["Pressure"].astype(int)
    df["Wind-Speed"] = df["Wind-Speed"].astype(int)
    df["Kelvin-Temp"] = df["Kelvin-Temp"].astype(int)
    df["Celsius-Temp"] = df["Celsius-Temp"].astype(int)
    #Feels_Like_C = Temp_C - ((100 - Humidity)/5)
    df["FeelsLikeC"] = df["Celsius-Temp"] - ((100 - df["Humidity"])/5)
    
    df["Extreme_"] = 0 
    df.loc[(df["Celsius-Temp"] > 40) | (df["Celsius-Temp"] < 0),"Extreme_"] = 1

    df.to_csv("Collecting-Data-Learn/API/all-colleting-data.csv",mode='w',index=False)
    print(df)


"""clean_data()""" # if data file cleaning data 


def visualization():
    # Plot a line chart showing temperature trends across cities over time.
    df = pd.read_csv("Collecting-Data-Learn/API/all-colleting-data.csv")

    fig, ax = plt.subplots(2,2)

    sns.lineplot(data=df,ax=ax[0,0],x="City",y="Celsius-Temp")
    ax[0,0].tick_params(axis='x', rotation=90) 
    ax[0,0].set_title("Temperatures In Cities")
    
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr,ax=ax[0,1],annot=True,cmap="coolwarm",linecolor="black")
    ax[0,1].set_title("HeatMap")

    sns.barplot(ax=ax[1,0],data=df,x="City",y="FeelsLikeC")
    ax[1,0].tick_params(axis='x', rotation=25)
    ax[1,0].set_title("Feels-Like-C in Cities")

    sns.scatterplot(data=df,x="City",y="Wind-Speed")
    ax[1,1].tick_params(axis='x', rotation=25)
    ax[1,1].set_title("Wind Speed Analysis")
    
    plt.tight_layout()
    plt.savefig("Collecting-Data-Learn/API/graph-images/weather-analysis.png")
    plt.show()
visualization()



    
