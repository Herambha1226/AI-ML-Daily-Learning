import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv("matplotlib/project-on-matplotlib/data/students.csv")

plt.scatter(df["Hours_Studied"],df["Final_Score"])
plt.title("Study Hours vs Final Score")
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.savefig("matplotlib/project-on-matplotlib/output/comparison.png")
plt.show()