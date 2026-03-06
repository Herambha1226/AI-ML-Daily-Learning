# Feature Engineering : The Feature Engineering means Creating the new column on existing data.

# for example there is data of students the student data can categorized student based on dateofbirth or Age 
# or predict the who are healthy by using weight and age.

import pandas as pd 

df = pd.read_csv("DATA-CLEANING/datasets/Data-To-Use.csv")

df["FamilySize"] = df["sibsp"] + df["parch"] + 1 

print(df)