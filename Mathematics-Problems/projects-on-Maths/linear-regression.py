#  skeleton of the linear regression
# 1.data
# 2.parameter
# 3.prediction
# 4.loss
# 5.gradients
# 6.update

#    step 2:
# data: x,y
# parameter: w,b
# prediction: line equation
# loss: how wrong we are
# gradients: how to reduce error
# update: adjust w and b

import numpy as np

x =  np.array([1,2,3,4,5],dtype=float)
y = np.array([2,4,6,8,10],dtype=float)

w = 0.0    # weight (slope)
b = 0.0    # bias (intercept)
lr = 0.01  # learning rate  

for epoch in range(1000):
    # 3. Prediction (forward pass)
    y_pred = w * x + b

    # 4.loss (mean Squared error)
    loss = np.mean((y-y_pred))

    # 5. Gradients (how to reduce error)
    dw = np.mean(-2 * x * (y - y_pred))
    db = np.mean(-2 * (y - y_pred))

    # 6.update parameters
    w= w-lr*dw
    b= b-lr*db

    if epoch % 100 == 0:
        print(f"Epochs {epoch} | Loss: {loss:.4f}")


