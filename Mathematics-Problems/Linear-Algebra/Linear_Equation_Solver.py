import numpy as np

A = np.array([[2,1],
              [1,3]])
B = np.array([5,6])

det = np.linalg.det(A)
print("Determinant Of A : ",det)

if det != 0 :
    A_inverse = np.linalg.inv(A)
    print("Inverse Of A : ",A_inverse)

    x = A_inverse @ B
    print("Solution [x,y] : ",x)

    print("Verification Ax: ",A @ x)
else:
    print("No Unique Solutions At !")