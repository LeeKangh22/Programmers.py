import numpy as np
import random

def gradientDescent(X, y, w, alpha, m, numIterations):
    xTrans = X.transpose()
    for i in range(0, numIterations):
        h = np.dot(X, w)
        loss = h - y
        gradient = np.dot(xTrans, loss) / m
        w = w - alpha * gradient
    return w



def genData(numPoints, bias, variance):
    X = np.zeros(shape = (9, 4))
    y = np.zeros(shape = 9)
    for i in range(0, numPoints):     
        X[i][0] = 1
        X[i][1] = i  
        y[i] = (i + bias) + random.uniform(0, 1) * variance
    return X, y

