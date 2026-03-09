
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
# this is techniques for selecting k value. process of selecting k is Choose K -> check Prediction accuracy
 # -> modify K
def cross_validation():

    data = load_iris()

    x = data.data
    y = data.target

    x_train,x_test,y_train,y_test = train_test_split(
        x,y,test_size=0.2
    )

    k_values = range(1,20)
    accuracy = []

    for k in k_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train,y_train)

        pred = model.predict(x_test)
        acc = accuracy_score(y_test,pred)

        accuracy.append(acc)

        print("K = ",k," Accuracy = ",acc)
    
    best_k = accuracy.index(max(accuracy)) + 1 
    print("Best K : ",best_k)
    print("Best Accuracy : ", max(accuracy))

cross_validation()