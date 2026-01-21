import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma


x = np.linspace(0, 10, 1000)

shape = 5

rate = 1
y = gamma.pdf(x, a=shape, scale=1/rate)
plt.plot(x, y, label=r"$s=5,r=1$")

rate = 1.25
y = gamma.pdf(x, a=shape, scale=1/rate)
plt.plot(x, y, c="red", label=r"$s=5,r=1.25$")

rate = 2
y = gamma.pdf(x, a=shape, scale=1/rate)
plt.plot(x, y, c="green", label=r"$s=5,r=2$")

rate = 4
y = gamma.pdf(x, a=shape, scale=1/rate)
plt.plot(x, y, c="lightblue", label=r"$s=5,r=4$")

plt.legend()

plt.xlabel(r"$X$")
plt.ylabel(r"$f(x)$")
plt.title("Funkcja gęstości")
plt.show()
