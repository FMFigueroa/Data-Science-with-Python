import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-100,101,1)       # Array x
y1 = 25 * x ** 2 - 2 * x        # y1 = 0.5x²+2x
y2 = ((0.5 * x ** 2) // 2 * x)  # y2 = ½x²/2x
y3 = np.sin(0.25 * x) * 250000  # y3= 250K sin(¼x)

#================================================
plt.plot(x,y1,'r')
plt.plot(x,y2,'b--')
plt.plot(x,y3,'y')
plt.grid(True)
plt.show()