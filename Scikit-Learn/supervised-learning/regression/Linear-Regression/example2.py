from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

data = pd.read_csv("Scikit-Learn//supervised-learning//regression//Linear-Regression//dataset//headbrain.csv")
print(data.shape)
print(data.head())

x = data["Head Size(cm^3)"].values
y = data["Brain Weight(grams)"].values

n = len(x)

X = x.reshape((n,1))

reg = LinearRegression()
reg = reg.fit(X,y)

y_pred = reg.predict(X)

mse = mean_squared_error(y,y_pred)
rmse = np.sqrt(mse)
r2_score = reg.score(X,y)

print(np.sqrt(mse))
print(r2_score)