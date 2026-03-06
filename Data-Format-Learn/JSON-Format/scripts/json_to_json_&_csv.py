import json
import pandas as pd 

data = {
    "name":"Gayathri",
    "age" : 18,
    "city" : "Hyderabad",
    "qualification" : "MBBS"
}
def json_(data):
    with open("Data-Format-Learn/JSON-Format/data/output-json.json",'w') as f:
        json.dump(data,f,indent=4)
json_(data)

def dataframe(data):
    df= pd.DataFrame([data])
    df.to_json("Data-Format-Learn/JSON-Format/data/output-pandas.json",orient="records",indent=4)
dataframe(data)

def convert_csv(data):
    df =pd.DataFrame([data])
    df.to_csv("Data-Format-Learn/JSON-Format/data/output-pandas.csv",index=True,encoding="utf-8")
convert_csv(data)