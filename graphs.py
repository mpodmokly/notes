import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f


x = np.linspace(0, 4, 1000)

df1 = 1
df2 = 1
y = f.pdf(x, df1, df2)
plt.plot(x, y, c="C0", label=r"$d_1=1,d_2=1$")

df1 = 2
df2 = 1
y = f.pdf(x, df1, df2)
plt.plot(x, y, c="red", label=r"$d_1=2,d_2=1$")

df1 = 5
df2 = 2
y = f.pdf(x, df1, df2)
plt.plot(x, y, c="green", label=r"$d_1=5,d_2=2$")

df1 = 100
df2 = 100
y = f.pdf(x, df1, df2)
plt.plot(x, y, c="lightblue", label=r"$d_1=100,d_2=100$")

plt.legend()
plt.xlabel(r"$X$")
plt.ylabel(r"$f(x)$")
plt.title("Funkcja gęstości")
plt.show()
