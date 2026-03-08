import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(50,10,1000)
#print("Histogram using Data : ",data)
plt.hist(data,bins=20)
plt.title("Histogram - Data Distribution")
plt.xlabel("values")
plt.ylabel("frequency")
plt.show()

plt.boxplot(data)
plt.title("Box Plot")
plt.show()

x = np.random.rand(100)
y = 3*x + np.random.rand(100)*0.2
plt.scatter(x,y)
plt.title("Scatter Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

days = np.arange(1,21)
sales = np.random.randint(50,100,20)
plt.plot(days,sales)
plt.title("Sales Trend")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()

categories = ["A","B","C"]
values = [10,25,15]
plt.bar(categories,values)
plt.title("Bar Chart")
plt.show()


import seaborn as sns
import pandas as pd
df = pd.DataFrame({
    "x1":np.random.rand(100),
    "x2":np.random.rand(100),
    "x3":np.random.rand(100)
})

sns.heatmap(df.corr(),annot=True)

plt.show()