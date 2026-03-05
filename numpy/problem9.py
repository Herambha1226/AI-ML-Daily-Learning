"""   
A = np.array([[2, 0],
              [0, 3]])
Tasks:

Find eigenvalues using np.linalg.eig()

Find eigenvectors

Verify the equation:

A · v = λ · v
"""
import numpy as np 

A = np.array([[2, 0],
              [0, 3]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print('Eigenvalues : \n',eigenvalues)
print("Eigenvectors : \n",eigenvectors)