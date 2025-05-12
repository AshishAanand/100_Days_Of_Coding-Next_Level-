import matplotlib.pyplot as plt
import numpy as np

# Line plot

# def f(x):
#     return x**2 + 2*x**3 + 1 + 3*x + 4 + 5*x**2 + 6*x**3 + 7*x + 8 + 9*x**2 + 10*x**1000 + 11*x + 12

# # Create data
# x = np.linspace(0, 10, 100)
# y = f(x) # I figured out graph of polinomial is affected by the highest degree term not by the coefficients


# # Create plot
# plt.plot(x, y)
# plt.title('Sine Wave')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.grid(True)
# plt.show()

# Scatter plot

# Create data
# x = np.random.rand(50)
# y = np.random.rand(50)
# colors = np.random.rand(50) # this gives the color of points
# area = (30 * np.random.rand(50))**2 # this gives the size of points

# # Create plot
# plt.scatter(x, y, s=area, c=colors, alpha=0.5) # s is the size of points, c is the color of points, alpha is the transparency
# plt.title('Scatter Plot')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# Bar plot

# Create data
# categories = ['A', 'B', 'C', 'D', 'E']
# values = [25, 40, 30, 55, 15]

# # Create plot
# plt.bar(categories, values, alpha=0.5, color='blue') # align is the alignment of the bars, alpha is the transparency, color is the color of the bars
# plt.title('Bar Plot')
# plt.xlabel('Category')
# plt.ylabel('Value')
# plt.show()

# Histogram
# Create data
data = np.random.randn(1000)

# Create plot
plt.hist(data, bins=30, alpha=0.5, color='blue', edgecolor='black') # bins is the number of bins, alpha is the transparency, color is the color of the bars, edgecolor is the color of the edges of the bars
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

print("Working")