#  Feature Scaling : Some ML models sensitive ti feature size 
# Example : 
# AGE : 25
# Salary : 50000
# Salary Dominates the model 
# we scale it

#Standardization 
import pandas as pd 
from sklearn.preprocessing import StandardScaler,LabelEncoder


df = pd.read_csv("DATA-CLEANING/datasets/Data-To-Use.csv")

# in the data has the Gender/sex data that datatype is string so it rises error without labelencoder.

# this is use finding all columns are strings 
categorical_cols = df.select_dtypes(include=['object','string']).columns

# encoding the srting column 
le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# now scale because all are numbers
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

print(df_scaled)