import numpy as np 

X = np.array([[1],[2],[3],[4],[5],[6]])
y = np.array([0,0,0,1,1,1])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

w = 0
b = 0
learning_rate = 0.02
ephocs = 10000

for i in range(ephocs):
    z = w * X + b 

    y_pred = sigmoid(z)

    error = y_pred - y.reshape(-1,1)

    dw = np.mean(error * X)
    db = np.mean(error)

    w = w - learning_rate * dw 
    b = b - learning_rate * db

def predict(X):
    z = w * X + b 

    probs = sigmoid(z)

    return (probs >= 0.5).astype(int)

prediction = predict(X)
print("Prediciton : ",prediction.flatten())



import matplotlib.pyplot as plt 

X_vis = np.linspace(0,7,100).reshape(-1,1)

z = w * X_vis + b 
y_vis = sigmoid(z)

plt.plot(X_vis,y_vis,label="Sigmoid Curve")

plt.scatter(X,y,color="red",label ="Training Data")

boundary = -b / w 
plt.axvline(boundary,linestyle="--",label="Decision Boundary")

plt.xlabel("x")
plt.ylabel("Probability")
plt.title("Logistic Regression Visualization")
plt.legend()
plt.savefig("Scikit-Learn/supervised-learning/classification/Logistic-regression/logistic-visualization.png")
plt.show()
