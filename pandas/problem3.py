import pandas as pd 
data = {
    "Name" : ["Ram","Ram","Sam","Riya"],
    "Age" : ["20","20","21",None]
}
df = pd.DataFrame(data)

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Convert Age to Integer 

print(df.dtypes)
df["Age"] = pd.to_numeric(df["Age"],errors="coerce")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Age"] = df["Age"].astype(int)

print("Clean Data : ",df)