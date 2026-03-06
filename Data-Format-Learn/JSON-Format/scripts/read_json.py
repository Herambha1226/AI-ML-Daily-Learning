import json
import pandas as pd 

def json_(file):
    with open(file,'r') as f:
        data = json.load(f)
    print(data)
json_(file="Data-Format-Learn/JSON-Format/data/data.json")

def dataframe(file):
    df = pd.read_json(file)
    print(df)
dataframe(file="Data-Format-Learn/JSON-Format/data/data.json")