# Random Forest Model on iris data
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = load_iris()

x = data.data
y = data.target

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.3,random_state=42
)

model = RandomForestClassifier(n_estimators=100)

model.fit(x_train,y_train)

pred = model.predict(x_test)

print("Accuracy : ",accuracy_score(pred,y_test))