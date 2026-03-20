import numpy as np 

x = np.array([1,2,3,4,5])
y = np.array([5,10,15,20,25])

y_pred = np.full(len(y),y.mean())

g = y_pred - y  # gradient
h = np.ones(len(y)) # hessian

lambda_ = 1 

w = - np.sum(g) / (np.sum(h) + lambda_)
print("Leaf Value: ",w)

learning_rate = 0.1 

y_pred = y_pred + learning_rate * w 
print("Updated Prediction : ",y_pred)


