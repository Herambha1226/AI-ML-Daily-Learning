# Gradient Boosting Building from scratch 
import numpy as np 
from sklearn.tree import DecisionTreeRegressor

x = np.array([[1],[2],[3],[4],[5]])
y = np.array([5,10,15,20,25])


F = np.full(len(y),y.mean())

models = []

learning_rate = 0.1
n_estimators = 5 

for i in range(n_estimators):

    residuals = y - F 

    tree = DecisionTreeRegressor(max_depth=1)
    tree.fit(x,residuals)

    pred = tree.predict(x)

    F = F + learning_rate * pred

    models.append(tree)

    print(f"iteration {i+1}, Prediction: {F}")

