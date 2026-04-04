from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np


data = fetch_california_housing()

x = data.data 
y = data.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

model = ElasticNet(alpha=0.1,l1_ratio=0.7)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test,y_pred)
print("Mean Squared Error : ",mse)

print("\n Feature Name Of DataSet : \n")
for name,coef in zip(data.feature_names,model.coef_):
    print(f"{name} : {coef}")


