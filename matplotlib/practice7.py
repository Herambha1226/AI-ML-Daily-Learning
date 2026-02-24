# 📊 Practice 2: Age Distribution (Real Dataset Style)

import matplotlib.pyplot as plt 

ages = [18,19,20,18,21,22,19,20,23,24,18,21,22,20]

plt.hist(ages)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number Of People")

plt.show()