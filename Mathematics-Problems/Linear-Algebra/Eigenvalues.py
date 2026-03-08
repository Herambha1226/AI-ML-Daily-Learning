import numpy as np

A = [[3, 0],
     [0, 1]]

eigenvalues,eigenvectors = np.linalg.eig(A)

print("Eigenvalues (strengths/importance): ",eigenvalues)
print("Eigendirection (directions) : ",eigenvectors)

B = [[1, 1],
     [1, 1]]
#a) Find eigenvalues
#b) One eigenvalue is zero — what does that mean physically?
eigenvalues,eigenvectors = np.linalg.eig(B)
print("Eigenvalues (strengths/importance): ",eigenvalues)
print("Eigendirection (directions) : ",eigenvectors)
