import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


x = np.linspace(-3, 5, 1000)
sigma = 1

mu = 0
y = norm.pdf(x, loc=mu, scale=sigma)
plt.plot(x, y, c="C0", label=r"$\mu=0,\sigma=1$")

mu = 1
y = norm.pdf(x, loc=mu, scale=sigma)
plt.plot(x, y, c="red", label=r"$\mu=1,\sigma=1$")

mu = 2
y = norm.pdf(x, loc=mu, scale=sigma)
plt.plot(x, y, c="green", label=r"$\mu=2,\sigma=1$")

plt.legend()
plt.xlabel(r"$X$")
plt.ylabel(r"$f(x)$")
plt.title("Funkcja gęstości")
plt.show()
