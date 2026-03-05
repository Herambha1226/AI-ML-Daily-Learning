"""   
Find dot product using np.dot()

Verify using manual formula:

a1*b1 + a2*b2 + a3*b3


Check shape of result
"""
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

dot  = np.dot(a,b)
print("Dot Product Of Two Arrays : ",dot)

manual = 0 
for i in range(len(a)):
    manual += a[i] * b[i]

print("Manual : ",manual)
print("Numpy : ",dot)