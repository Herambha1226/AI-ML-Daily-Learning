# 🤖 Practice 1: Height vs Weight (Feature Relationship)

import matplotlib.pyplot as plt 

height = [150,155,160,165,170,175,180]
weight = [50,55,60,65,70,75,80]

plt.scatter(height,weight)

plt.title("Height vs Weight Relationship")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")

plt.show()
