import numpy as np 
import matplotlib.pyplot as plt 

X = np.array([
    [1,2],
    [2,3],
    [3,3],
    [6,7],
    [7,8],
    [8,8]
])

y = np.array([-1,-1,-1,1,1,1])

w = np.zeros(2)
b = 0 

learning_rate = 0.01
lambda_param = 0.01
epochs = 1000

for _ in range(epochs):
    for i,x_i in enumerate(X):
        condition = y[i] * (np.dot(x_i,w) + b) >= 1

        if condition:
            w = w - learning_rate * (2 * lambda_param * w)
        else:
            w = w - learning_rate * (2 * lambda_param * w - np.dot(x_i,y[i]))
            b = b - learning_rate * y[i]
print("Weights : ",w)
print("Bias : ",b)
