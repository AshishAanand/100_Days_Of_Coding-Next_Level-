from sklearn.linear_model import LinearRegression
import numpy as np

# Linear Model
# Sample data

X = np.array([2, 3, 4, 5 ,6 ,7 ,8, 9, 10]).reshape(-1, 1)

Y = np.array([100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000])
# Create a linear regression model

model = LinearRegression()
# Fit the model to the data

model.fit(X, Y) # Now our mini model is ready to make pridictions
# Predict the price of a house with 11 rooms

predicted_price = model.predict([[11]])

print(f"Predicted price of a house with 11 rooms: {predicted_price}")
print(f"Model Coefficient: {model.coef_}") # Weights
# The slope of the line
print(f"Model Intercept: {model.intercept_}") # The y-intercept of the line
# The point where the line crosses the y-axis
# The model is a linear regression model, which means it tries to find the best-fitting line through the data points.


new_prediction = model.coef_ * 12 + model.intercept_

print(f"New prediction for 12 rooms {new_prediction}")

# print(X)
