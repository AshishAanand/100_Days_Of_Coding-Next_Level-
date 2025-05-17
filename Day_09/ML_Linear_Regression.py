from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10]) # House rooms
Y = np.array([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000])

model = LinearRegression()

model.fit(X, Y)

print(model.predict([[11]]))

print("working")