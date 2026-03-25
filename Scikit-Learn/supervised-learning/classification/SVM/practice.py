import numpy as np
import matplotlib.pyplot as plt

x = np.array([
    [1,2],
    [2,3],
    [3,3],
    [6,5],
    [7,7]
])

y = np.array([-1,-1,-1,1,1])

w = np.zeros(x.shape[1])
b = 0

learning_rate = 0.01
lambda_program = 0.01
epochs = 1000

for epoch in range(epochs):
    for i in range(len(x)):
        condition = y[i] * (np.dot(w, x[i]) + b) >= 1

        if condition:
            w = w - learning_rate * (2 * lambda_program * w)
        else:
            w = w - learning_rate * (2 * lambda_program * w - y[i] * x[i])
            b = b - learning_rate * (-y[i])

def predict(x):
    approx = np.dot(x,w) + b
    return np.sign(approx)

print("Weights : ",w)
print("Bias: ",b)

print("Prediction : ",predict(x))

for i in range(len(x)):
    if y[i] == -1:
        plt.scatter(x[i][0], x[i][1],marker='o')
    else:
        plt.scatter(x[i][0],x[i][1],marker='x')
def hyperplane(x_val,w,b,offset):
    return (-w[0] * x_val - b + offset) / w[1]

x_vals = np.linspace(0,8,100)

y_vals = hyperplane(x_vals,w,b,0)

y_vals_p = hyperplane(x_vals,w,b,1)
y_vals_n = hyperplane(x_vals,w,b,-1)

plt.plot(x_vals,y_vals)
plt.plot(x_vals,y_vals_p)
plt.plot(x_vals,y_vals_n)

plt.title("SVM Decision Boundary with Margins")
plt.xlabel("x1")
plt.xlabel("x2")

plt.show()