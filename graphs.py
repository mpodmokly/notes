import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


n = 21
x = np.arange(0, n)

l = 1
prob = poisson.pmf(x, l)

for i in range(n):
    if i == 0:
        plt.scatter(x[i], prob[i], c="C0", label=r"$\lambda=1$")
    else:
        plt.scatter(x[i], prob[i], c="C0")

l = 4
prob = poisson.pmf(x, l)

for i in range(n):
    if i == 0:
        plt.scatter(x[i], prob[i], c="red", label=r"$\lambda=4$")
    else:
        plt.scatter(x[i], prob[i], c="red")

l = 10
prob = poisson.pmf(x, l)

for i in range(n):
    if i == 0:
        plt.scatter(x[i], prob[i], c="green", label=r"$\lambda=10$")
    else:
        plt.scatter(x[i], prob[i], c="green")

plt.xlabel("X")
plt.ylabel("p(x)")
plt.title("Funkcja prawdopodobieństwa")
plt.legend()
plt.show()
