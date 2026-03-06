# DATA Preprocessing : Convert raw data into ML usable data 

# Note : Most ML algorithms only accepts numbers.

# Example Problem : 
# Gender
# Male
# Female
# Male

# Machine can't understand text . So , Convert it.

from sklearn.preprocessing import LabelEncoder
import pandas as pd 

df = pd.read_csv("DATA-CLEANING/datasets/Data-To-Use.csv")

le = LabelEncoder()

df["sex"] = le.fit_transform(df["sex"])
print(df)