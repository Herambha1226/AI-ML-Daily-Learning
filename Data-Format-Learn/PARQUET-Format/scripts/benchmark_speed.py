import pandas as pd 
import time

start = time.perf_counter()
df = pd.read_json("Data-Format-Learn/PARQUET-Format/data/student.json")
print("JSON READ Time : ",time.perf_counter() - start)

start = time.perf_counter()
df = pd.read_parquet("Data-Format-Learn/PARQUET-Format/data/student.parquet")
print("Parquet read time : ",time.perf_counter() - start)