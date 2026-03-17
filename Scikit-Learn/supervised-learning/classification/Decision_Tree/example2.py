# Decison Tree Applied From Scratch 
import numpy as np 
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6])
y = np.array([0,0,0,1,1,1])

def gini(y):
    classes = np.unique(y)
    print("Classes: ",classes)
    impurity = 1
    for c in classes:
        p = np.sum(y == c)/len(y)
        print(p)
        impurity -= p**2
    return impurity

def best_split(x,y):
    best_gini = 1
    best_threshold = None

    for t in x :
        left = y[x <= t]
        right = y[x > t]

        if len(left) == 0 or len(right) == 0:
            continue

        gini_left = gini(left)
        gini_right = gini(right)

        weighted_gini = (
            len(left)/len(y)*gini_left +
            len(right)/len(y)*gini_right
        )

        if weighted_gini < best_gini:
            best_gini = weighted_gini
            best_threshold = t 
    return best_threshold,best_gini

threshold_value, gini_value = best_split(x,y)
print("Threshold Value : ",threshold_value)
print("Best Gini : ",gini_value)

plt.scatter(x,y)

plt.axvline(x=threshold_value,linestyle='--')

plt.xlabel("Features")
plt.ylabel("Class")
plt.title("Decision Tree Split Visualization")
plt.show()

