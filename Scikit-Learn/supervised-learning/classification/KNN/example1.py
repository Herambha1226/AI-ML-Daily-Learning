# This is one of the example program of the K-NN 

# import Necessary modules for K-NN 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def manual_k_value():
    # load data
    data = load_iris()

    x = data.data 
    y = data.target 

    # split data
    x_train,x_test,y_train,y_test = train_test_split(
        x,y,test_size=0.2
    )

    # create model 
    model = KNeighborsClassifier(n_neighbors=5)

    # Train 
    model.fit(x_train,y_train)

    # Prediction pupose use
    prediction = model.predict(x_test)

    print("Prediction : ",prediction)

manual_k_value()
