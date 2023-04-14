import numpy as np


class LinearRegression:
    def __init__(self, learning_rate=0.001, number_iterations=1000):
        self.learning_rate = learning_rate
        self.number_iterations = number_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        number_samples, number_features = X.shape
        self.weights = np.zeros(number_features)
        self.bias = 0

        for _ in range(self.number_iterations):
            y_pred = np.dot(X, self.weights) + self.bias

            # Partial Derivatives
            dw = (1 / number_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / number_samples) * np.sum(y_pred - y)

            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
