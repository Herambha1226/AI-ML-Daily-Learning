# Using Some Styles in Histogram 
import matplotlib.pyplot as plt 

data = [12,15,14,10,18,20,22,25,30,28,26,24]

plt.hist(data,bins=4,color="skyblue",edgecolor="black")

plt.title("Data Distribution Analysis")
plt.xlabel("Values")
plt.ylabel("Freaquency")
plt.grid(axis="y")

plt.show()