from sklearn.linear_model import LinearRegression
import numpy as np

lr = LinearRegression()
X = np.random.random([10, 6])
y = np.random.random(10)

intercept = True

if intercept:
    X = np.c_[np.ones(X.shape[0]), X]

sigma = np.linalg.pinv(X.T @ X)
beta = np.atleast_2d(sigma @ X.T @ y)

## GridSearchCV
##