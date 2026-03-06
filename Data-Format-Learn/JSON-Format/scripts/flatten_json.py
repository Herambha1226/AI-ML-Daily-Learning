import json
import pandas as pd

data = {
    "name" : "Herambha",
    "marks" : {"math":90,"chemestry":91,"java":95}
}
def json_(data):
    with open("Data-Format-Learn/JSON-Format/data/output-json1.json","w") as f:
        json.dump(data,f,indent=4)
json_(data)

def data_normalization(data):
    df = pd.json_normalize(data)
    print(df)
data_normalization(data)

def convert_csv(data):
    df = pd.json_normalize(data)
    df.to_csv("Data-Format-Learn/JSON-Format/data/output-csv.csv",index=False)
convert_csv(data)