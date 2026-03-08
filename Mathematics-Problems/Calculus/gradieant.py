# One-variable gradient descent
def loss(w,x,y_true):
    return (w*x - y_true)**2
def gradient(w,x,y_true):
    return 2*(w*x - y_true)*x
w = 0
lr = 0.01

for i in range(15):
    grad = gradient(w,2,8)
    w = w - lr * grad
    print(f"step {i} : w={w:.3f}, loss ={loss(w,2,8):.3f}")
