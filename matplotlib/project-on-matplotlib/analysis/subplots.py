import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv("matplotlib/project-on-matplotlib/data/students.csv")

x = df["Name"]
y = df["Final_Score"]

fig, ax = plt.subplots(1,2)

ax[0].plot(x,y)
ax[0].set_title("Marks Trend")
ax[0].set_xlabel("Names")
ax[0].set_ylabel("Marks")

ax[1].hist(y,bins=5)
ax[1].set_xlabel("Marks")
ax[1].set_ylabel("Number Of Students")
ax[1].set_title("Marks Distribution")

plt.tight_layout()

plt.savefig("matplotlib/project-on-matplotlib/output/subplot.png")
plt.show()
