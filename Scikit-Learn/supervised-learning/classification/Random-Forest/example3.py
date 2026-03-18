# Now this below code tells the overfitting of model

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = load_iris()

x = data.data
y = data.target
feature_names = data.feature_names

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.3,random_state=42
)

model = RandomForestClassifier(n_estimators=10)

model.fit(x_train,y_train)

pred = model.predict(x_test)
print("Accuracy Score : ",accuracy_score(pred,y_test))

importance = model.feature_importances_

for name,score in zip(feature_names,importance):
    print(f"{name} : {score}")
print("\n=== Deep Trees ===")
model1 = RandomForestClassifier(max_depth=None,n_estimators=100)
model1.fit(x_train,y_train)
train_pred = model1.predict(x_train)
test_pred = model1.predict(x_test)

print("Train Accuracy : ",accuracy_score(train_pred,y_train))
print("Test Predict : ",accuracy_score(test_pred,y_test))

model2 = RandomForestClassifier(max_depth=3, n_estimators=100)
model2.fit(x_train, y_train)

train_pred2 = model2.predict(x_train)
test_pred2 = model2.predict(x_test)

print("\n=== Shallow Trees ===")
print("Train Accuracy:", accuracy_score(y_train, train_pred2))
print("Test Accuracy:", accuracy_score(y_test, test_pred2))