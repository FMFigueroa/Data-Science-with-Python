import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,100,0.2)
y1 = np.sin(x)
y2 = x ** 2 + 2 * x
y3 = np.log(x)
y4 = x + 2
#==========================================
plt.figure(1)
ax1 = plt.subplot(211) # (rows|columns|index)
ax1.plot(x,y1)
ax2 = plt.subplot(212) # (rows|columns|index)
ax2.plot(x,y2,'y--')
#==========================================
plt.figure(2)
plt.plot(x,y1,'r--')
#==========================================
plt.figure(3)
ax3 = plt.subplot(212) # (rows|columns|index)
ax3.plot(x,y3,'r')
ax4 = plt.subplot(211) # (rows|columns|index)
ax4.plot(x,y4,'g')
#==========================================
plt.show()