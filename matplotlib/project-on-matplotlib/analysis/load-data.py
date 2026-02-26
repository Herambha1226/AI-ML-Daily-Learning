import pandas as pd 
import matplotlib.pyplot as plt 

# load data
df = pd.read_csv("matplotlib/project-on-matplotlib/data/students.csv")

# Display the head 
print(df.head(n=2))

# Basic info of data 
print("\nDataset Information : ")
print(df.info())

# statical summary
print(df.describe())