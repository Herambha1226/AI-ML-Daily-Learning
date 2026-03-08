import numpy as np

print(" \t\t All Types Of Matrices Are Shown Below !")

row_matrix = np.array([1,3,5])
print("Row MAtrix:\n",row_matrix)

col_matrix = np.array([[1],[2],[3]])
print("Column Matrix:\n",col_matrix)

square_matrix = np.array([12,11,26,25])
print("Square Matrix:\n",square_matrix)
print("Shape: ",square_matrix.shape)

rectangle_matrix = np.array([[3,1,5],[4,7,1]])
print("Rectangle Matrix :\n",rectangle_matrix)

diagonal_matrix = np.array([[1,0,0],[0,2,0],[0,0,3]])
print("Diagonal Matrix :\n",diagonal_matrix)

scalar_matrix = np.array([[2,0,0],[0,2,0],[0,0,2]])
print("Scalar Matrix :\n",scalar_matrix)

unit_matrix = np.array([[1,0,0],[0,1,0],[0,0,1]])
print("Unit Matrix :\n",unit_matrix)

zero_matrix = np.array([[0,0,0],[0,0,0],[0,0,0]])
print("Zero Matrix:\n",zero_matrix)

upper_triangle_matirix = np.array([[1,7,2],[0,2,4],[0,0,5]])
print("Upper Traingle Matrix :\n",upper_triangle_matirix)

lower_triangle_matrix = np.array([[1,0,0],[2,3,0],[4,5,6]])
print("Lower Traingle Matrix :\n",lower_triangle_matrix)

symmetric_matrix = np.array([[1,3,-5],[3,2,1],[-5,1,-3]])
print("Symmetric Matrix :\n",symmetric_matrix)

skew_symmetric_matrix = np.array([[0,3,-5],[-3,0,1],[5,-1,0]])
print("Skew Symmetric Matrix :\n",skew_symmetric_matrix)

