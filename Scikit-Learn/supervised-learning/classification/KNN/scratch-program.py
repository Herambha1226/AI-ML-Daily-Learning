# This is KNN ALgorithm uses without using the sicikit learn

import numpy as np 
from collections import Counter

def euclidean_distance(a,b):
    return np.sqrt(np.sum((a-b)**2))

def knn_prediction(x_train,y_train,x_test,k):

    distance = []

    for i in  range(len(x_train)):
        dist = np.sqrt(np.sum((x_train[i] - x_test)**2))
        distance.append((dist,y_train[i]))

    distance.sort()

    neighbors = distance[:k]

    labels = [label for _,label in neighbors]

    most_common = Counter(labels).most_common(1)

    return most_common[0][0]


# Test the KNN Algorithm without using scikit-learn for K-NN 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data = load_iris()

x = data.data 
y = data.target

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2
)

prediction = []
for x in x_test:
    pred = knn_prediction(x_train,y_train,x,k=3)
    prediction.append(pred)

accuracy = np.sum(prediction == y_test) / len(y_test)

print("Accuracy : ",accuracy)
