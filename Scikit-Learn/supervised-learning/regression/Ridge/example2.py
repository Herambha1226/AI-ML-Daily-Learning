import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error,r2_score

data = fetch_california_housing()

x = data.data
y = data.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = Ridge(alpha=1.0)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print("MSE : ",mse)
print("R2 : ",r2)

plt.scatter(y_test,y_pred)
min_val = min(y_test.min(),y_pred.min())
max_VAL = max(y_test.max(),y_pred.max())

plt.plot([min_val,max_VAL],[min_val,max_VAL])

plt.xlabel("Actual")
plt.ylabel("Prediction")
plt.title("Ridge Regression Result")
plt.show()