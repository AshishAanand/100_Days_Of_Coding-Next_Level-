import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a simple line plot

# def f(x):
#     return x**3 + 2*x + 1

# x = np.linspace(-10, 10, 100)
# y = f(x)

# # Create plot with two y-axes
# fig, ax1 = plt.subplots(figsize=(10, 6))

# # First plot (left y-axis)
# ax1.plot(x, y, 'b-')
# ax1.set_xlabel('x')
# ax1.set_ylabel('sin(x)', color='b')
# ax1.tick_params(axis='y', labelcolor='b')

# # Second plot (right y-axis)
# ax2 = ax1.twinx()
# ax2.plot(x, -y, 'r-')
# ax2.set_ylabel('cos(x)', color='r')
# ax2.tick_params(axis='y', labelcolor='r')

# plt.title('Two scales')

# Create a 3D plot
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(projection='3d')

# # Create data
# x = np.linspace(-5, 5, 50)
# y = np.linspace(-5, 5, 50)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(np.sqrt(X**2 + Y**2))

# # Surface plot
# # surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
# # 3D wireframe
# surf = ax.plot_wireframe(X, Y, Z, color='black')
# fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('3D Surface Plot')

# plt.show()



# Create a figure and axis
fig, ax = plt.subplots()

# Initialize plot with blank data
line = ax.plot([], [], 'r-')
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

# Define update function for animation
def update(frame):
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x + frame/10)
    line.set_data(x, y)
    return line

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Save animation
# ani.save('animation.gif', writer='pillow', fps=20)

plt.show()
