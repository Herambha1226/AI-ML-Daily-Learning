#  y=(2x+3)*2

def forward(x):
    u = 2*x + 3
    y = u**2
    return y
def backward(x):
    u = 2*x + 3
    dy_du = 2*u
    du_dx = 2
    return dy_du*du_dx

x = 4
print("y=",forward(x))
print("dy/dn=",backward(x))

