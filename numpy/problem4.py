"""
Perform element-wise multiplication

Perform matrix multiplication using:

np.dot()

@ operator

np.matmul()

Explain why results are different
"""
import numpy as np

A = [[1,2],
     [3,4]]
B = [[5,6],
     [7,8]]

A_ele_5 = A * 5
B_ele_5 = B * 5
print("A Matrix Element-Wise Multiplication : \n",A_ele_5)
print("B Matrix Element-Wise Multiplication : \n",B_ele_5)

dot = np.dot(A,B)
print("Dot Of A & B : ",np.dot(A,B))
A_ = np.array(A)
B_ = np.array(B)
print("@ using Multiplication : ",A_ @ B_)
print("np.matmul() using for multiplication 2 Matrixes : ",np.matmul(A,B))

