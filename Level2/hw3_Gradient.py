import numpy as np
import random

def gradientDescent(X, y, w, alpha, m, numIterations):
    xTrans = X.transpose()
    for i in range(0, numIterations):
        h = np.dot(X, w)
        loss = h - y
        cost = np.sum(loss ** 2) / (2 * m)
        print("Iteration %d | Cost: %f" % (i, cost))
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

X, y = genData(100, 25, 10)
m, n = np.shape(X)

alpha = 0.0005
w = np.ones(n)
w = gradientDescent(X, y, w, alpha, m, 9)
print(w)