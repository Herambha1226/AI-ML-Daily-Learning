import numpy as np

# create array
a = np.array([1,2,3,4,5])
print("Array : \n",a)

# create zeros array
b = np.zeros((2,5))
print("Zeros :\n",b)

# creates ones array
c = np.ones((2,5))
print("Ones : \n",c)

# creates a list with from number to number
d = np.arange(0,20)
print("Start to End : \n",d)

# creates evenly spaced numbers
e = np.linspace(0,10,5)
print("Evenly Spaced List : \n",e)

# random numbers between 0 and 1
f = np.random.rand(2,3)
print("Random Numbers b/w 0 and 1 : \n",f)

# Generate random integers 
g = np.random.randint(1,10,5)
print("Random numbers : \n",g)

# --------------------------- Important Properties ------------------------------ #
arr = np.array([2,4,6,7,8,9])

print("Array Data Type : \n",arr.dtype)

print("Array Shape : \n",arr.shape)

print("Array Size : \n",arr.size)

print("Dimension of Array : \n",arr.ndim)
