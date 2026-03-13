import numpy as np 
import matplotlib.pyplot as plt
from sklearn import svm 
 
# Create simple dataset
X = np.array([
    [1,2],
    [2,3],
    [3,3],
    [2,1],
    [3,2],
    [7,8],
    [8,8],
    [9,10],
    [8,9],
    [9,8]
])

y = np.array([0,0,0,0,0,1,1,1,1,1])

model = svm.SVC(kernel='linear')
model.fit(X,y)

plt.scatter(X[:,0],X[:,1],c=y,cmap='coolwarm')

ax = plt.gca()
xlim = ax.get_xlim()
y_lim = ax.get_ylim()

xx = np.linspace(xlim[0],xlim[1],30)
yy = np.linspace(y_lim[0],y_lim[1],30)

YY,XX = np.meshgrid(yy,xx)
xy = np.vstack([XX.ravel(),YY.ravel()]).T 

Z = model.decision_function(xy).reshape(XX.shape)

ax.contour(
    XX,YY,Z,
    colors='black',
    levels=[-1,0,1],
    alpha=0.6,
    linestyle=['--','-','--']
)

ax.scatter(
    model.support_vectors_[:,0],
    model.support_vectors_[:,1],
    s=150,
    facecolors='none',
    edgecolors='black'
)

plt.title("SVM Data Seperation Visualization")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()