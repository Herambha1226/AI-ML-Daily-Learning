import requests 
import pandas as pd 
from datetime import datetime
import time 

API_KEY = "28529f3a8c4ae80afcc3fa1ae09856de"
city = "uppugunduru"

def collect_data():
    print("Collecting Data Starts ....")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url)
    if response.status_code == 200:
        print("API is Ready To Use ....")
    data = response.json()

    df = pd.json_normalize(data)

    df = df[["name","main.temp","main.humidity","main.pressure"]]

    # converts temperature to celcius 
    df["Temp_celsius"] = df["main.temp"] - 273.15
    df["Time Stamp"] = datetime.now()

    df.rename(columns={
        "name":"City",
        "main.temp":"Kelvin Temperature",
        "main.humidity":"Humidity",
        "main.pressure":"Pressure"
    },inplace=True)
    with open("weather_data.csv",'a') as f:
        df.to_csv(f,mode='a',header=True,index=False)
    print("Data Collected and Stored In File ...")

collect_data()

#print("Selected Columns Data Of Weather : \n",df)
