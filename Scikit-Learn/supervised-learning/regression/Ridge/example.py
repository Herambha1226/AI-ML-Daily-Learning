import numpy as np

class RidgeRegression:
    def __init__(self,lr=0.01,n_iters=1000,lamda=0.1):
        self.lr = lr
        self.n_iters = n_iters
        self.lamda = lamda
        self.w = None
        self.b = None

    def fit(self,x,y):
        n_samples,n_features = x.shape

        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iters):
            y_pred = np.dot(x,self.w) + self.b

            dw = (-2 * np.dot(x.T,(y - y_pred)) / n_samples) \
                   + 2 * self.lamda * self.w
            
            db = -2 * np.sum(y - y_pred) / n_samples

            self.w -= self.lr * dw
            self.b -= self.lr * db

    def predict(self,x):
        return np.dot(x,self.w) + self.b
    


