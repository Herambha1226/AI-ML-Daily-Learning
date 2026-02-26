import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

x = [1,2,3,4,5]
y = [10,20,25,30,40]
z = [5,15,10,20,25]

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.scatter(x,y,z)

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("3D Scatter Plot")

plt.savefig("matplotlib/graph-images/3d_scatter.png",dpi=300,bbox_inches = "tight")
plt.show()