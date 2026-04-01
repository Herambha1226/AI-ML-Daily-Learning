# import libraries

import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error,r2_score

def load_data():
    data = fetch_california_housing()
    x,y = data.data,data.target
    return x,y

def split_data(x,y):
    return train_test_split(x,y,test_size=0.2,random_state=42)

def train_model(x_train,y_train,alpha=0.1):
    model = Lasso(alpha=alpha)
    model.fit(x_train,y_train)
    return model

def evaluate_model(model,x_test,y_test):
    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test,y_pred)
    r2 = r2_score(y_test,y_pred)

    print("Model Performance")
    print(f"MSE : {mse:4f}")
    print(f"R2 Score : {r2:.4f}")

    return y_pred

def plot_predicition(y_test,y_pred):
    plt.figure(figsize=(6,6))
    plt.scatter(y_test,y_pred)

    min_val = min(y_test.min(),y_pred.min())
    max_val = max(y_test.max(),y_pred.max())

    plt.plot([min_val,max_val],[min_val,max_val])

    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("Actual vs Predicted (Lasso Regression)")
    plt.show()

def plot_coefficients(model):
    plt.figure(figsize=(8,4))
    plt.bar(range(len(model.coef_)),model.coef_)

    plt.xlabel("Feature Index")
    plt.ylabel("Coefficient Value")
    plt.title("Lasso Feature Importance")
    plt.show()


def plot_lasso_path(x_train,y_train):
    alphas = np.logspace(-2,1,20)
    coefficients = []

    for alpha in alphas:
        model = Lasso(alpha=alpha)
        model.fit(x_train,y_train)
        coefficients.append(model.coef_)
    
    coefficients = np.array(coefficients)

    plt.figure(figsize=(8,5))

    for i in range(coefficients.shape[1]):
        plt.plot(alphas,coefficients[:,i])
    
    plt.xscale("log")
    plt.xlabel("Alpha (Regularization Strength)")
    plt.ylabel("Coefficeint Value")
    plt.title("Lasso Path")
    plt.show()

def main():

    x,y= load_data()

    x_train,x_test,y_train,y_test = split_data(x,y)

    model = train_model(x_train=x_train,y_train=y_train,alpha=0.1)

    y_pred = evaluate_model(model,x_test,y_test)

    plot_predicition(y_test,y_pred)
    plot_coefficients(model)
    plot_lasso_path(x_train,y_train)

if __name__ == "__main__":
    main()