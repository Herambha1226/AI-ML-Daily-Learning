""" 
2x + y = 5
x + y = 3
Tasks:

Convert equations into matrix form AX = B

Use np.linalg.solve() to find x and y

Verify solution manually

(Hint: A = coefficients matrix)
"""
import numpy as np

A = [[2,1],
     [1,1]]
B = [5,3]

solution = np.linalg.solve(A,B)
print("Linear Algebra Solution : ", solution)

