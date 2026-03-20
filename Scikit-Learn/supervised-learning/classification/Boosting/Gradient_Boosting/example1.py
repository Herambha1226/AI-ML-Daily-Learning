# Learning from previous mistakes using math optimization to gradually improve predictions
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data = load_iris()

x = data.data 
y = data.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42,stratify=y)


model = GradientBoostingClassifier()

model.fit(x_train,y_train)

print(model.score(x_test,y_test))
