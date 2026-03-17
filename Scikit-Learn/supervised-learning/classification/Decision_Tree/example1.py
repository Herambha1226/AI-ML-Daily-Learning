# importing necessary modules
from sklearn.tree import DecisionTreeClassifier,plot_tree
import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
])
y = np.array([0,0,0,1,1,1])

model = DecisionTreeClassifier(max_depth=2)
model.fit(x,y)

prediction = model.predict([[2.5]])
print("Prediction : ",prediction)

x_vis = np.linspace(1,6,100).reshape(-1,1)
y_pred = model.predict(x_vis)

plt.scatter(x,y,color="red",label="data")
plt.plot(x_vis,y_pred,label="Decision Boundary")

plt.title("Decision Tree Boundary")
plt.xlabel("Features")
plt.ylabel("class")
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
plot_tree(model,filled=True)
plt.title("Decision Tree Structure")
plt.show()
