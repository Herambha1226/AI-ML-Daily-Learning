# Feature Selection : The Feature Selection means select only useful data / useful column in the exising data.

# this feature selection can useful for developing the model by using required data 

# for example speed of car 
# Example Columns : distance and time 

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("DATA-CLEANING/datasets/Data-To-Use.csv")

plt.bar(df["survived"],df["age"])
plt.title("Survived Based Age !")
plt.xlabel("Survived")
plt.ylabel("Age")
plt.show()
