import numpy as np
import matplotlib.pyplot as plt

n = 5
l = 3
dx = l/n
t_int = 100
t_end = 200
a = 0.01
k = 10

T = np.zeros(n)
T_old = np.zeros(n)

T[0] = t_int
T[n-1] = t_end

tol = 1e-4
err = 1
while err > tol:
  for j in range(0, k):
    T_old =T
    for i in range(1, n-1):
      T[i] =  0.5*(T[i+1] + T[i-1])
      err = np.max(np.max(np.abs(T_old-T)))

solved = np.linspace(0.0, l, n)

fig, ax = plt.subplots()
ax.plot(solved,T);
ax.set_xlim(0,l);
plt.show()
