"""A = np.array([[4, 7],
              [2, 6]])
Tasks:

Find determinant using np.linalg.det()

Find inverse using np.linalg.inv()

Verify:

A @ A_inv ≈ Identity Matrix  """
import numpy as np

A = np.array([[4, 7],
              [2, 6]])
det = np.linalg.det(A)
inverse_A = np.linalg.inv(A)
print("Det Of A : ",det)
print("Inverse Of A : ",inverse_A)
verify = A @ inverse_A
print("Is Identity (A @ inverse_A) : \n",verify)
