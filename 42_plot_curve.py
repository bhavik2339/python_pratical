# 42. Plot a curve
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = x ** 2

plt.plot(x, y)
plt.title("Curve: y = x²")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
