# Standardization : 
# formula : z = (x - mean) / std
# the above formula is used for all numerical values or selected values

from sklearn.preprocessing import StandardScaler,LabelEncoder
import pandas as pd 

df = pd.read_csv("DATA-CLEANING/datasets/Data-To-Use.csv")

categorical_col = df.select_dtypes(include=["object","string"]).columns

le = LabelEncoder()
for col in categorical_col:
    df[col] = le.fit_transform(df[col])

scaler = StandardScaler()

df_scaled = scaler.fit_transform(df)

print(df_scaled)