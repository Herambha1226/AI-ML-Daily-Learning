import numpy as np 
from collections import Counter

x = np.array([
    ["sunny"],
    ["sunny"],
    ["Rainy"],
    ["Rainy"]
])
y = np.array(["No","No","Yes","Yes"])


def entropy(y):
    counts = Counter(y)
    print("Counts : ",counts)
    total =  len(y)
    print("Total Size : ",total)

    ent = 0
    for count in counts.values():
        p = count / total
        ent += -p * np.log2(p)
        print("Entropy : ",ent)
    return ent

def information_gain(x_column,y):
    parent_entropy = entropy(y)

    values = np.unique(x_column)
    weighted_entropy = 0

    for val in values:
        indices = np.where(x_column == val)
        subset_y = y[indices]

        weighted = len(subset_y) / len(y)
        weighted_entropy += weighted * entropy(subset_y)

    return parent_entropy - weighted_entropy
    
def best_split(x,y):
    best_gain = -1 
    best_feature = None

    for col in range(x.shape[1]):
        gain = information_gain(x[:,col],y)
        print(f"Feature {col} Gain : {gain}")

        if gain > best_gain:
            best_gain = gain
            best_feature = col
    return best_feature

def build_tree(x,y):
    if len(set(y)) == 1:
        return y[0]
    
    feature = best_split(x,y)

    tree = {}
    values = np.unique(x[:,feature])
    for val in values:
        indices = np.where(x[:,feature] == val)
        subtree = build_tree(x[indices],y[indices])

        tree[val] = subtree
    return tree

import random

def bootstrap(x,y):
    n = len(x)
    indices = np.random.choice(n,n,replace=True)
    return x[indices],y[indices]

def random_forest(x,y,n_trees=5):
    forest = []
    for i in range(n_trees):
        x_sample,y_sample = bootstrap(x,y)
        single_tree = build_tree(x_sample,y_sample)
        forest.append(single_tree)
    return forest

def predict_tree(tree,x):
    if not isinstance(tree,dict):
        return tree
    
    feature_value = x[0]

    if feature_value in tree:
        return predict_tree(tree[feature_value],x)
    else:
        return None
    
def predict_forest(trees,X):
    predictions = []

    for x in X:
        tree_pred = []

        for tree in trees:
            tree_pred.append(predict_tree(tree,x))

        final = Counter(tree_pred).most_common(1)[0][0]
        predictions.append(final)

    return predictions

trees = random_forest(x,y,n_trees=3)
print("Trees : ",trees)

pred = predict_forest(trees,x)
print("Prediction: ",pred)
