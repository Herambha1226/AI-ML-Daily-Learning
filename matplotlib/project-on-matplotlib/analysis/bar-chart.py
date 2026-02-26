import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv("matplotlib/project-on-matplotlib/data/students.csv")

plt.bar(df["Name"],df["Final_Score"])
plt.title("Subject Wise Marks Comparision")
plt.xlabel("Scores")
plt.ylabel("Number Of Students")
plt.savefig("matplotlib/project-on-matplotlib/output/bar_chart.png")
plt.show()