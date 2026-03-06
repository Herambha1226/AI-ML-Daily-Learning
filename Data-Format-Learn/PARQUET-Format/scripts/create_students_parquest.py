import pandas as pd 
import json

# converting XL format to json 

def convert_xl_to_josn():
    df =pd.read_excel("Data-Format-Learn/EXCEL-Format/data/STUDENT-DATA.xlsx")
    df.to_json("Data-Format-Learn/PARQUET-Format/data/student.json",indent=4,)
#convert_xl_to_josn()


def data():
    with open("Data-Format-Learn/PARQUET-Format/data/student.json",'r') as f:
        data = json.load(f)
    return data

# converting JSON to PARQUET

def create_parquet():
    df = pd.DataFrame([data()])
    df.to_parquet("Data-Format-Learn/PARQUET-Format/data/student.parquet",index=False)
    print("Students.parquet file created successfully")
create_parquet()