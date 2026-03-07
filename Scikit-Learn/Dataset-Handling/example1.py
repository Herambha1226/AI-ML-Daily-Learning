# load the built-in datasets in the scikit-learn

# load built-in data set
from sklearn.datasets import load_iris

data = load_iris()

print("iris contain data : ",data)

print("Data Set Structure : ",data.keys())

# Feature / Target Seperation

x = data.data
y = data.target

print("x shape :",x.shape)
print("y Shape : ",y.shape)

print("Feature Names : ",data.feature_names)

print("Target Classes : ",data.target_names)

import pandas as pd 

df = pd.DataFrame(x,columns=data.feature_names)
df["flower"] = y 

df["species"] = df["flower"].map({
    0:"setosa",
    1:"versicolor",
    2:"virginica"
})

print("Converted data into DAtaFrame : \n",df.head())

# Train Test Split 
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)

print(x_train.shape)
print(x_test.shape)
