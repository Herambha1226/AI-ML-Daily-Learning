# DATA Cleaning : Remove errors and bad data which in data

# DATA Cleaning Operations:
 # Missing Values  : isnull()
 # Duplicates      : drop_duplicates()
 # Data Types      : astype()
 # Outliers        : outliers = df[(df[column_name] < lower_bound) | (df[column_name] > upper_bound)]
 # Invalid values  : replace()
  
import pandas as pd 

df = pd.read_csv("DATA-CLEANING/datasets/Data-To-Use.csv")

# Check Missing Value 
print(df.isnull().sum())

# delete duplicates
df = df.drop_duplicates()

# fill missing values with mean
df["age"] = df["age"].fillna(df["age"].mean())

# delete row with missing values
df = df.dropna()

print(df)

# Check Missing Value 
print(df.isnull().sum())

