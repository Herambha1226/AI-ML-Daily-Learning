import pandas as pd 
import matplotlib.pyplot as plt 

df =pd.read_csv("matplotlib/project-on-matplotlib/data/students.csv")

plt.hist(df["Final_Score"],bins=5)
plt.title("Marks Distribution of Final Score")
plt.xlabel("Scores")
plt.ylabel("Number of Stdents")
plt.savefig("matplotlib/project-on-matplotlib/output/marks-distibution.png",dpi=300)
plt.show()
