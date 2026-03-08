"""Logistic Regression (Binary Classifier)
Goal: predict YES / NO (0 or 1)

Examples:

pass / fail

spam / not spam

disease / no disease"""


import numpy as np

x = np.array([1,2,3,4,5],dtype=float)
y = np.array([2,4,6,8,10],dtype=float)

w = 0.0
b = 0.0
lr = 0.01

def sigmoid(z):
    return 1/(1+np.exp(-z))
for epoch in range(1000):

    y =w * x + b
    y_pred = sigmoid(y)

    loss = -np.mean(
        y*np.log(y_pred + 1e-8) + 
        (1 - y) * np.log(1 - y_pred + 1e-8)
    )

    dw = np.mean((y_pred-y)*x)
    db = np.mean(y_pred-y)

    w = w - lr * dw
    b = b - lr *db

    if epoch % 100 == 0:
        print(f"epoch {epoch} | loss: {loss:.4f}")
        