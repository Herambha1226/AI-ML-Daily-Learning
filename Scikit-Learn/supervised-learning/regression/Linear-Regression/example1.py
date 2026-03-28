import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
plt.rcParams['figure.figsize'] = (20.0,10.0)

data = pd.read_csv("Scikit-Learn//supervised-learning//regression//Linear-Regression//dataset//headbrain.csv")
print(data.shape)
print(data.head())

x = data["Head Size(cm^3)"].values
y = data["Brain Weight(grams)"].values

mean_x = np.mean(x)
mean_y = np.mean(y)

n = len(x)

number = 0 
denom = 0

for i in range(n):
    number += (x[i] - mean_x) * (y[i] - mean_y)
    denom += (x[i] - mean_x) ** 2

b1 = number / denom
b0 = mean_y - (b1 * mean_x)

print(b1,b0)

max_x = np.max(x) + 100
min_x = np.min(x) - 100

lin_x = np.linspace(min_x,max_x,1000)
lin_y = b0 + b1 * lin_x

plt.plot(lin_x,lin_y,color="#58b970",label= "Regression Line")

plt.scatter(x,y,c="#ef5423",label = "Scatter Plot")

plt.xlabel("Head Size in cm3")
plt.ylabel("Brain Weight in grams")
plt.legend()
plt.show()

ss_t = 0 
ss_r = 0
for i in range(n):
    y_pred = b0 + b1 * x[i]
    ss_t += (y[i] - mean_y) ** 2
    ss_r += (y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print(r2)
