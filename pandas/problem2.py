import pandas as pd 
data = {
    "Name" : ["Anu","Vijay","Rohit","Sneha"],
    "Age" : [20,None,19,22],
    "Marks" : [78,92,None,88]
}
df = pd.DataFrame(data)

# Check missing values count
mis_count = df.isnull().sum()
print("Missing Value Count : \n",mis_count)

# Fill missing Age with mean
df["Age"]=df["Age"].fillna(df["Age"].mean())

# Fill missing Marks with median
df["Marks"]=df["Marks"].fillna(df["Marks"].median())

#  Print cleaned dataset
print("Cleaned Data : \n",df)