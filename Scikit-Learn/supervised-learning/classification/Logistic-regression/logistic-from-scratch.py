import numpy as np

X = np.array([[1],
              [2],
              [3],
              [4],
              [5],
              [6]])

y = np.array([0,0,0,1,1,1])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

weights = 0 
bias = 0 
learning_rate = 0.01
epochs = 10000

for i in range(epochs):

    z = weights * X + bias

    y_pred = sigmoid(z)

    error = y_pred - y.reshape(-1,1)

    dw = np.mean(error * X)
    db = np.mean(error)

    weights = weights - learning_rate * dw 
    bias = bias - learning_rate * db

def predict(X):
    z = weights * X + bias

    probs = sigmoid(z)

    return (probs >= 0.5).astype(int)

prediction = predict(X)
print("Prediction: ",prediction.flatten())


