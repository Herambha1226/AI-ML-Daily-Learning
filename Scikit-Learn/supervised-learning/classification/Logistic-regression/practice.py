# model builds from scratch by using small dataseet 
import math

x = [1,2,3]
y = [0,0,1]

w = 0
b = 0
learn_rate = 0.1
epochs = 1000

for epoch in range(epochs):
    total_loss = 0
    for i in range(len(x)):
        z = w * x[i] + b
        y_hat = 1 / (1 + math.exp(-z))

        loss = -(y[i] * math.log(y_hat) + (1-y[i]) * math.log(1-y_hat))
        total_loss += loss

        dw = (y_hat - y[i]) * x[i]
        db = (y_hat - y[i])
        
        w =  w - learn_rate * dw
        b = 0 - learn_rate * db

    if epoch % 100 == 0:
        print(f"Epoch {epoch},Loss : {total_loss:.4f} ")
print("Final w : ",w)
print("Final b : ",b)


def predict(x_val):
    z = w * x_val + b
    y_hat = 1 / (1 + math.exp(-z))

    if y_hat >= 0.5:
        return f"Predciton : 1"
    else:
        return f"Prediction : 0"
    
print(predict(5))
