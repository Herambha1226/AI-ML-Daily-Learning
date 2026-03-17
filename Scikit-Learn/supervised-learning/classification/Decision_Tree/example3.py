# Another Problem on decison tree it solves using manual caliculations of gini and best split
import numpy as np 
import matplotlib.pyplot as plt 

# Hours studied and sleep hours
x = np.array([
    [2,8],
    [3,7],
    [4,6],
    [5,5],
    [6,4],
    [7,3]
])
# 0 -> Not Pass
# 1 -> Pass
y = np.array([0,0,0,1,1,1])

def gini(y):
    classes = np.unique(y)
    impurity = 1
    for c in classes:
        p = np.sum(y==c)/len(y)
        impurity -= p**2
    return impurity

def best_split(x,y):
    best_gini = 1
    best_threshold = None
    best_feature = None
    
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
                best_threshold = t
                best_feature = feature
    return best_threshold,best_gini,best_feature

threshold,best_gini,feature = best_split(x,y)

print("Threshold Value : ",threshold)
print("Gini : ",best_gini)
print("Features : ",feature)

study = x[:,0]
sleep = x[:,1]

colors = ["red" if i == 0 else "green" for i in y]
plt.scatter(study,sleep,c=colors)

if feature == 0:
    plt.axvline(x=threshold,linestyle="--")
else:
    plt.axhline(y=threshold,linestyle="--")

plt.xlabel("Features")
plt.ylabel("Classes")
plt.title("Decision Tree For 0 = Not Pass , 1 = Pass")

import matplotlib.patches as mpatches
not_pass = mpatches.Patch(label="Not Pass (0)",color="red")
pass_ = mpatches.Patch(label="Pass (1)",color="Green") 
plt.legend(handles=[not_pass,pass_])
plt.show()

