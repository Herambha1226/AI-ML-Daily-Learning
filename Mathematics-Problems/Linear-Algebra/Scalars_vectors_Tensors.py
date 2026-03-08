import numpy as np

print("Scalar Practice : A Scalar is a Just A Single Number \n ")
a = 2
b = 10
z = a**2 + 10
print("Scalar Addition : ",z)
print("SCalar Subtraction : ",b-a)
print('Scalar Multiplication : ',b*a)
print("Scalar Division : ",a/b)

print("Vector Practice : A Vector is having both the magnituted(lenght/size) and direction . It is a 1D array ! \n")
c = np.array([4,5,6])
d = np.array([8,9,7])
print("Vector Addition : ",c+d)
print("Vector Subtraction :",c-d)
print("Vector Multiplication : ",c@d)
print("Vector Division : ",c/d)
print(" Vector Multiply using Scalar : ",4 * c)
print("Vector Dot operation : ",np.dot(c,d))

print("Matrix Practice : A Matrix is known as 2D dimensional . It has rows and columns.")
e = np.array([[1,2,3],[4,5,6]])
f = np.array([[9,8,7],[4,3,6]])
print("Matrices Addition : \n",e+f)
print("Matrices Subtraction : \n",e-f)
print("Matrices Multiplication : \n",e*f)
print("Matric Multiply using Scalar : \n",4 * e)
print("Matrices Division : ",e/f)
print("Matrix multiplication using vector : \n",c*e)

print("Tensor Practice : A Tensor is Multi Dimenstional .")
g = np.array([[[5,6,7],[9,3,4]],[[1,3,2],[6,2,4]]])
print("Tensor : \n",g)

print("Grandient Problem : example ( wx + b )")
w = np.array([7,5,3])
x = np.array([9,3,2])
b = 0.5
print("Gradient : ",np.dot(w,x)+b)

print("Loss Function Pridection : ")
h_true = 10
b_pred = 8
loss = (h_true - b_pred)**2
print("Loss : ",loss)
