import numpy as np

# Problem 1 — Broadcasting + Arithmetic
""" 
Perform A + B

Perform A * B

Subtract 5 from all elements of A (without loop)

Divide each element of A by 2
"""

A = np.array([[2,4,6],
              [1,3,5]])
B = np.array([10,20,30])

print("A + B : \n",A+B)
print("A * B : \n",A*B)
print("A - 5 : \n",A-5)
print("A / 2 : \n",A/2)


#  🔥 Problem 2 — Axis Mastery (Very Important)
""" 
Sum of each column

Sum of each row

Mean of each column

Maximum value in each row

Index position of global maximum value
"""
M = np.array([[5,10,15],
              [20,25,30],
              [35,40,45]])
print("Sum Of Each Column : ",np.sum(M,axis=1))
print("Sum Of Each Row : ",np.sum(M,axis=0))
print("Mean Of Each Column : ",np.mean(M,axis=1))
print("Minimum Value in Each Row : ",np.min(M,axis=0))
print("Index Position Of Each Maximum Value : ",np.argmax(M))


#  🔥 Problem 3 — Standardization (Real ML Use Case)
""" 
Compute column-wise mean

Compute column-wise standard deviation

Perform feature scaling:
"""
X = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
print("Column Wise Mean : ",np.mean(X,axis = 1))
print("Column Wise Standard Deviation : ",np.std(X,axis=1))
X_Scaled = (X - np.mean(X))/np.std(X)
print("Perform Feature Scaling : ",X_Scaled)

# 🔥 Problem 4 — Reshape Logic
"""
Reshape into (3,4)

Reshape into (4,3)

Transpose the (3,4) matrix

Flatten it

Ravel it

Modify first element of raveled array and observe if original changes
"""
arr = np.arange(1,13)
mat_3_4 = arr.reshape(3,4)
print("Reshape Matrix 3 x 4 : ",mat_3_4)
print("Reshape Matrix 4 x 3 : ",arr.reshape(4,3))
print("Transepose Of 3 x 4 Matrix : ",mat_3_4.T)
print("Ravel : ",arr.ravel())


# 🔥 Problem 6 — Stacking & Concatenation
""" 
Vertical stack

Horizontal stack

Concatenate along axis=0

Concatenate along axis=1

Stack using np.stack()
"""
a = np.array([[1,2],
              [3,4]])
b = np.array([[5,6],
              [7,8]])

print("Vertical Stack : ",np.vstack((a,b)))
print("Horizontal Stack : ",np.hstack((a,b)))
print("Concatenate Along axis = 0 :  ",np.concatenate((a,b),axis=0))
print("Concatenate Along axis = 1 :  ",np.concatenate((a,b),axis=1))
print("Stack : ",np.stack((a,b)))

# 🔥 Problem 7 — Split + Index Logic + Arg Functions
"""
Find global maximum value

Find its index using argmax

Find minimum value row-wise

Split array into 3 equal row parts

From each split, find mean value

Using boolean indexing, extract values greater than 50
"""
arr2 = np.array([[12,45,78],
                 [23,56,89],
                 [34,67,90]])
print("global maximum value : ",np.max(arr2))
print("Index of the Max Value : ",np.argmax(arr2))
print("Minimum Value Row-Wise : ",np.min(arr2,axis=0))
print("Array Split into 3 equal parts : ",np.split(arr2,3))
print("Extract Valeus Greater Than 50 : ",arr2 > 50)