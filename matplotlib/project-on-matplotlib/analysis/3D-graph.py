import matplotlib.pyplot as plt 
import pandas as pd 
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("matplotlib/project-on-matplotlib/data/students.csv")

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")

x = df["Hours_Studied"]
y = df["Attendance"]
z = df["Final_Score"]

ax.scatter(x,y,z)

ax.set_xlabel("Hours Studied")
ax.set_ylabel("Attendence")
ax.set_zlabel("Final Score")
ax.set_title("3D Student Performance Analysis")

plt.savefig("matplotlib/project-on-matplotlib/output/3d-graph.png")
plt.show()