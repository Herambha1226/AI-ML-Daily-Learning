import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x**2 - 6*x + 5
def derivative(x,h=0.0001):
    return (f(x+h)-f(x))/h 
x_vals = np.linspace(0,6,400)
y_vals = f(x_vals)

der_vals = derivative(x_vals)
min_index = np.argmin(np.abs(der_vals))

x_min = x_vals[min_index]
y_min = f(x_min)

plt.figure()
plt.plot(x_vals,y_vals,label = "f(x)=x^2-6x+5")
plt.scatter(x_min,y_min)
plt.text(x_min,y_min,f' Min ({x_min:.2f}),({y_min:.2f})')
plt.title("Dervative & Optimization")
plt.legend()
plt.show()



