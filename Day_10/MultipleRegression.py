from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Multiple Linear Regression
# Sample data

X = np.array([  # [rooms, bathrooms, year]
    [2, 1, 2],
    [3, 2, 3],
    [4, 2, 4],
    [5, 3, 5],
    [6, 3, 6],
    [7, 4, 7],
    [8, 4, 8],
    [9, 5, 9],
    [10, 5, 10]
]) # This house data is not real because their values are not real and dosen't make sence also its just for testing

Y = np.array([100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000])

# Create a multiple regression model

model = LinearRegression()

model.fit(X, Y)  # Now our mini model is ready to make predictions
# Predict the price of a house with 11 rooms, 5 bathrooms, and 11 years old

predicted_price = model.predict([[11, 5, 11]])
print(f"Predicted price of a house with 11 rooms, 5 bathrooms, and 11 years old:{predicted_price}")

print(f"Model Coefficient: {model.coef_}")  # Weights
# The slope of the line
print(f"Model Intercept: {model.intercept_}")  # The y-intercept of the line

# The point where the line crosses the y-axis
# Ploting the predictions
plt.scatter(X[:, 0], Y, color='blue', label='Actual Data')  # Actual data points (X[:, 0] is rooms)
plt.scatter(11, predicted_price, color='red', label='Predicted Price')  # Predicted price point
plt.plot(X[:, 0], model.predict(X), color='green', label='Regression Line')  # Regression line
# Regression line
plt.xlabel('Rooms')
plt.ylabel('Price')
plt.title('Multiple Linear Regression')
plt.legend()
plt.show()
