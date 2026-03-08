# plot fuction exaple
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-3,3,400)

f = x**3
df = 3 * x**2

plt.figure()
plt.plot(x,f,label="f(x) = x^3")
plt.plot(x,df,label="f(x) = 3x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Function of Derivatives")
plt.legend()
plt.show()
