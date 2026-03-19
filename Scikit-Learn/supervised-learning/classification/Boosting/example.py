# boosting is technique for incresing accuracy and speed of ML model 
# these are 3 types :
# 1.AdaBoosting
# 2.Gradient Boosting
# 3.XGBoosting (Extreme Gradient Boosting)

# example of Boosting 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_iris()

x = data.data 
y = data.target 

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42) # random state for stable split and same accurtacy evry time. 42 number is commonly used in programming.

weak_model = DecisionTreeClassifier(max_depth=1)

model = AdaBoostClassifier(estimator=weak_model,n_estimators=50,learning_rate=1)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print("Accuracy : ",accuracy_score(y_test,y_pred))
