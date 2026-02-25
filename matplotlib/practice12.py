import matplotlib.pyplot as plt 

#data 
data = [10,20,30,40,50]

plt.subplot(2,2,1)
plt.plot(data)
plt.title("Line Plot")

plt.subplot(2,2,2)
plt.bar(range(len(data)),data)
plt.title("Bar Chart")

plt.subplot(2,2,3)
plt.hist(data)
plt.title("Histogram")

plt.subplot(2,2,4)
plt.scatter(range(len(data)),data)
plt.title("Scatter Plot")

plt.show()