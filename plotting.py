#matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
v = 1
a = 0.2

x = np.linspace(0, 10, 11)
y =v*a*np.sinc(a*x)

plt.plot(x, y, 'o', color='black')
plt.show()