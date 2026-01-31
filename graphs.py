import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t


x = np.linspace(-5, 5, 1000)

nu = 1
y = t.pdf(x, df=nu)
plt.plot(x, y, c="C0", label=r"$\nu=1$")

nu = 5
y = t.pdf(x, df=nu)
plt.plot(x, y, c="red", label=r"$\nu=5$")

nu = 10
y = t.pdf(x, df=nu)
plt.plot(x, y, c="green", label=r"$\nu=10$")

plt.legend()
plt.xlabel(r"$X$")
plt.ylabel(r"$f(x)$")
plt.title("Funkcja gęstości")
plt.show()
