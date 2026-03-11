# Import Libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.datasets import load_breast_cancer

import numpy as np 
import pandas as pd 

# load the built-in dataset frmo sklearn
data = load_breast_cancer()

# Explring the dataset 
x = data.data 
y = data.target

# Split the dataset for using training and testing data
x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2,random_state=42 
)

# Check the Dataset shape 
print("X Data Shape : ",x.shape)
print("Y Data Shape : ",y.shape)

# Create Logistic regression model
model = LogisticRegression()

#train the model
model.fit(x_train,y_train)

#make prediciton
prediciton = model.predict(x_test)

#predict probabilites of all data in dataset
probabilites = model.predict_log_proba(x_test)

# accuracy checking 
accuracy = accuracy_score(y_test,prediciton)
print("Accuracy: ",accuracy)

# checking model parameters
print(model.coef_)
print(model.intercept_)
print(model.classes_)

#confusion matrix 
cm = confusion_matrix(y_test,prediciton)

print("Confusion matrix : \n",cm)


