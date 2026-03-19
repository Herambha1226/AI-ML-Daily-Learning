# AdaBoost from scratch
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

x = np.array([[1],[2],[3],[4],[5]])
y = np.array([1,1,-1,-1,1])

weights = np.ones(len(x)) / len(x)
print("Weights : ",weights)

models = []
alphas = []
accuracies = []

final_pred = np.zeros(len(x))

for _ in range(10): # i use 3 instead of 10 in range but it not give better accuracy so i change to 10.
    model = DecisionTreeClassifier(max_depth=1)
    
    model.fit(x,y,sample_weight=weights)

    pred = model.predict(x)

    for alpha,model in zip(alphas,models):
        final_pred += alpha * pred

    error = np.sum(weights * (pred != y))

    alpha = 0.5 * np.log((1 - error) / (error + 1e-10))

    weights *= np.exp(-alpha * y * pred)
    weights /= np.sum(weights)

    accuracies.append(accuracy_score(y,pred))
    
    models.append(model)
    alphas.append(alpha)


print("Alphas : ",alphas)
print("Models : ",models)
print("Accuracy : ",accuracies)

final_pred = np.sign(final_pred)
print("Final Accuracy : ",accuracy_score(y,final_pred))

plt.plot(range(1,len(accuracies)+1),accuracies,marker='o')
plt.title("Accuracy per Iteration")
plt.xlabel("Iteration")
plt.ylabel("Accuracy")
plt.show()
