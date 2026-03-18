# Using Yellowbrick module to showing accuracy of model

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from yellowbrick.classifier import ConfusionMatrix

data = load_iris()

x = data.data
y = data.target

x_train,x_test,y_train,y_test = train_test_split(
    x,y
)

model = RandomForestClassifier()
model._estimator_type = "classifier" 

viz = ConfusionMatrix(model)
viz.fit(x_train,y_train)
viz.score(x_test,y_test)
viz.show()