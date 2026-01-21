import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


plt.plot([0, 4], [0.25, 0.25])
plt.scatter([0, 4], [0.25, 0.25])

plt.plot([-3, 0], [0, 0], c="C0")
plt.plot([4, 7], [0, 0], c="C0")
plt.xlim(-2, 6)

# bottom = 
plt.ylim(plt.ylim()[0], 0.4)

plt.xlabel("X")
plt.ylabel("p(x)")
plt.title("Funkcja prawdopodobieństwa")
plt.show()
