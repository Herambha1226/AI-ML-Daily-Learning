import requests 
import pandas as pd 

API_KEY = "28529f3a8c4ae80afcc3fa1ae09856de"
city = "Hyderabad"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)

print("Status Code : ",response.status_code)
data = response.json()

print(data)