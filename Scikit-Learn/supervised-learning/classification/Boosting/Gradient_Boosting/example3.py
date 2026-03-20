# One Of the Pactice Problem on Gradient Boosting i apply from scratch 
from sklearn.tree import DecisionTreeRegressor
import numpy as np 

x = np.array([[1],[2],[3],[6],[4],[7],[5]])
y = np.array([10,20,30,40,50,70,60])

if len(x) == len(y):

    F = np.full(len(y),np.mean(y))

    models = []

    learning_rate = 0.1
    n_estimator = 3

    for i in range(n_estimator):

        residual = y - F

        tree = DecisionTreeRegressor(max_depth=1)
        tree.fit(x,residual)

        pred = tree.predict(x)

        F = F + learning_rate * pred

        models.append(tree)

        print(f"Iteration: {i+1},Predictions : {F},Residuals: {residual}")

