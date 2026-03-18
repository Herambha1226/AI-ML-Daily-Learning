# In the same code using which in the example1.py but this below code tells the feature importance score of model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import seaborn as sns 
import matplotlib.pyplot as plt

data = load_iris()

x = data.data
y = data.target
feature_names = data.feature_names

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.3,random_state=42
)

model = RandomForestClassifier(n_estimators=50)

model.fit(x_train,y_train)

pred = model.predict(x_test)

importance = model.feature_importances_
for name,score in zip(feature_names,importance):
    print(f"{name} : {score}")


print("Accuracy Score : ",accuracy_score(pred,y_test))

sns.barplot(x=feature_names,y=importance)
plt.title("Feature Importance")
plt.xlabel("Features Names")
plt.ylabel("Feature Score")
plt.show()