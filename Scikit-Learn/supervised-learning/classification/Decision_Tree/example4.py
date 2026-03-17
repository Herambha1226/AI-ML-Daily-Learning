# Another Problem on Loan Approval by using Decision Tree

import numpy as np
import matplotlib.pyplot as plt

x = np.array([
    [30,600],
    [35,650],
    [40,700],
    [50,720],
    [60,750],
    [70,800]
])

y = np.array([0,0,0,1,1,1])

def gini(y):
    classes = np.unique(y)
    impurity = 1 
    for c in classes:
        p = np.sum(y==c)/len(y)
        impurity -= p**2
    return impurity

def best_split(x,y):
    threshold =None 
    best_gini = 1 
    features = None 

    n_features = x.shape[1]

    for feature in range(n_features):
        values = x[:,feature]

        for t in values:
            left = y[values <= t]
            right = y[values > t]

            if len(left) == 0 or len(right) == 0:
                continue

            left_gini = gini(left)
            right_gini = gini(right)

            weighted_gini = (
                len(left)/len(y)*left_gini+
                len(right)/len(y)*right_gini
            )

            if weighted_gini < best_gini:
                best_gini = weighted_gini
                features = feature
                threshold = t 
    return best_gini,features,threshold
    
best_gini,features,threshold = best_split(x,y)

def predict(sample):
    if features == 0 :
        if sample[0] > threshold:
            return "Approved"
        else:
            return "Rejected"
    else:
        if sample[1] > threshold:
            return "Approved" 
        else:
            return "Rejected"


print("Best Gini : ",best_gini)
print("Features : ",features)
print("threshold : ",threshold)

print("Prediction : ",predict([45,710]))
