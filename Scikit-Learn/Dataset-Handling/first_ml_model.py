from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris  = load_iris()

x = iris.data 
y = iris.target

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2,random_state=42
)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(x_train,y_train)

predictions = model.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test,predictions)

print("Accuracy : ",accuracy)
