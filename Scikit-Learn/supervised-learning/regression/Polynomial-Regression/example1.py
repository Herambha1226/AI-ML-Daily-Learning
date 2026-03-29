import numpy as np
import matplotlib.pyplot as plt 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# data 
x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([1,4,9,16,25])

# polynomial transform 
poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)

model = LinearRegression()
model.fit(x_poly,y)


# pred 
pred = model.predict(x_poly)

plt.scatter(x,y)
plt.plot(x,pred)
plt.show()