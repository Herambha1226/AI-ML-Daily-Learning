import numpy as no
import random 
import matplotlib.pyplot as plt

a = [random.randint(1,10) for i in range(10)]
b = [random.randint(1,10) for i in range(10)]

plt.plot(a, b) 
plt.tiltle("Example Problem") 
plt.show() 