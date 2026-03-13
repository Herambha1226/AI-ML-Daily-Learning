# The Support Vector Machine example program 
# import neceserry packages
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data = load_iris()

x = data.data 
y = data.target

x_train,x_test,y_train,y_test = train_test_split(
    x,y,train_size=0.2,random_state=42
)

model = SVC(kernel='linear')

model.fit(x_train,y_train)

prediction = model.predict(x_test)
print("Prediction : ",prediction)
