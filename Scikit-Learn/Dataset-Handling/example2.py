# Load the built-in datasets in scikit-learn

# load built-in data set 
from sklearn.datasets import load_wine

data = load_wine()

print("Wine Data : ",data)

print("Data Set Structure : ",data.keys())


# Features and Targets Seperation 

x = data.data 
y = data.target 

print("X Shape : ",x.shape)
print("Y Shape : ",y.shape)

print("Feature Name : ",data.feature_names)
print("target Classes : ",data.target_names)

import pandas as pd
df = pd.DataFrame(x,columns=data.feature_names)
df["Wine"] = y

print("Converted Data into DataFrame : \n",df.head())

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)
print("X Train Shape : ",x_train.shape)
print("X Test Shape : ",x_test.shape)