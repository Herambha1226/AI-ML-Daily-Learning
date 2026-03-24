import numpy as np 

point = ['A','B','C','D','E']
x = [1,2,5,6,7]
y = [2,3,3,5,7]
cls = ["RED","RED","BLUE","BLUE","BLUE"]

data = {
    "point" : point,
    'x' : x,
    'y':y,
    "class" : cls
}

def eucliden_distance(px,py,x,y):
    return np.sqrt((px - x)**2 + (py - y)**2)

def pick_k(x):
    return int(np.sqrt(len(x)))

def knn(px,py):

    distance = []

    for i in range(len(x)):
        d = eucliden_distance(px,py,x[i],y[i])
        distance.append((cls[i], d))

    distance.sort(key=lambda t: t[1])

    k = pick_k(x)

    neighbours =distance[:k]

    votes = {}

    for label,dist in neighbours:
        weight = 1 / dist if dist != 0 else 1 
        votes[label] = votes.get(label,0) + weight

    return max(votes,key=votes.get)


    
print(knn(3,8))