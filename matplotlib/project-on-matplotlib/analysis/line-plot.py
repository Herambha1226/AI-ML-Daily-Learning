# A line plot can use for identify or knowing the marks trend
import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv("matplotlib/project-on-matplotlib/data/students.csv")

plt.plot(df["Name"],df["Final_Score"],marker='o')
plt.title("Student Final Score Trend Knowing using Line Plot")
plt.ylabel("Final Score")
plt.xlabel("Students")
plt.xticks(rotation=45)
plt.savefig("matplotlib/project-on-matplotlib/output/line-plot.png")
plt.show()