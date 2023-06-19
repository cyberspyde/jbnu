# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 13:26:35 2023

@author: USER
"""

from sklearn.datasets import load_diabetes
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.datasets import make_regression


import numpy as np

class LinearRegressionGD:
    def __init__(self, lr=0.01, n_iter=1000, l =0):
        self.lr = lr
        self.n_iter = n_iter
        self.weights = None
        self.bias = None
        self.l = l
        self.costs = []
        
    def fit(self, X, y):
        #initialize weights and bias
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        y_predicted = np.dot(X, self.weights) + self.bias

        #gradient descent algorithm
        for _ in range(self.n_iter):
            y_predicted = np.dot(X, self.weights) + self.bias
            
            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y)) + (self.l/n_samples)*self.weights
            db = (1/n_samples) * np.sum(y_predicted - y)
            
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            cost = (1/2*n_samples) * np.sum((y_train-y_predicted)**2) +( self.l / 2*n_samples)*np.sum(self.weights**2)
            self.costs.append(cost)
    
    def predict(self, X):
        
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted




X, y  = load_diabetes(return_X_y=True)
#X, y = make_regression(n_samples=100000, n_informative=80, n_features=250, noise=1, random_state=42)

X =X[:,2]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
#(X_train.shape,X_test.shape,y_train.shape, y_test.shape)

'''
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
'''

lr = LinearRegressionGD()
lr.fit(X_train,y_train)
y_pred = lr.predict(X_test)


print(r2_score(y_test,y_pred))

plt.plot(y_test[:200], color='r')
plt.plot(y_pred[:200], color='b')
plt.show()

plt.plot(lr.costs)
plt.show()

