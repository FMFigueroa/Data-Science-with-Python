import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('bmh')
#=============Tuples==========================
python = (85, 67, 23, 98)
java = (50, 67, 89, 14)
networking = (60, 20, 56, 22)
machine_learning = (88, 23, 10, 87)
#=========List of Name========================
peolple = ['Bob', 'Anna', 'John', 'Marks']
#=============================================
index = np.arange(4)
#=============================================
plt.bar(index, python, width=0.2, label="Python")
plt.bar(index + 0.2, java, width=0.2, label="Java")
plt.bar(index + 0.4, networking, width=0.2, label="Networking")
plt.bar(index + 0.6, machine_learning, width=0.2, label="Machine Learning")
#============Legend and Label==============================================
plt.title("IT Skill Levels")
plt.xlabel("Person")
plt.ylabel("Skill Level")
plt.xticks(index + 0.3, peolple)
plt.legend(loc='upper right')
plt.ylim(0, 150)
#==============================================
plt.show()


