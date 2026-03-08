import numpy as np

print("Scalar Equation : 3x+y")
x = np.array([3,5,4])
y = np.array([6,8,7])
z = (3*x)+y
print("Scalar Equation Solution : ",z)

print("Vector Addition : ")
z = np.array([10,20,40])
c =np.array([50,70,90])
print("Solution : ",z+c)


print("Dot Product : ")
v = np.array([12,10,34])
u = np.array([9,32,12])
print("Solution : ",np.dot(v,u))


print("Vector Norm : ")
n = np.array([6,12])
print("Solution : ",np.linalg.norm(n))


print("Matrix Vector Multipication : ")
e = np.array([[12,52,14],[62,2,1]])
f = np.array([13,11,24])
print("Solution : ",e@f)

print("Matrix Transepose : ")
g = np.array([[12,42],[12,53]])
print("Solution : ",g.T)

print("Matrix Mean : ")
h = np.array([[10,20,30],[12,22,32]])
print("Solution : ",np.mean(h))

print("Element Wise Square : ",h**2)

print("Loss : ")
y_true = np.array([20,40,60])
y_pred = np.array([10,30,50])
loss = (y_true - y_pred)**2
print("Solution : ",loss)
