import numpy as np

a = np.array([
    [1, 3, 4, 5],
    [4, 7, 9, 1],
    [7, 8, 8, 2]
])
#========Function Basics===============
# print(np.sqrt(a))
# print(np.log(a))
# print(np.exp(a))
# print(np.sin(a))
# print(np.cos(a))
# print(np.tan(a))
# print(np.sum(a))
# =====================================
# print(np.min(a))
# print(np.max(a))
# =====================================
# print(np.mean(a))
# print(np.median(a))
# print(np.std(a))
# =====================================
# b = a.reshape(2,2,3)
# print(b)
# =====================================
# print(a.flatten())
#======================================
# print(a.flat[7])
#======================================
# for x in a.flat:
#     print(x)
#======================================
# print(a.transpose())
#======================================



#======Other Arrays for Join===========

c = np.array([
    [1,2,3,7],
    [4,5,6,7],
    [7,8,9,7]
])

d = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [70,80,10,20]
])
#========Joining Arrays=========
# e = np.concatenate((c,d))
# print(e)
# print(e.shape)
#=======================================
# e2 = np.stack((c,d))
# print(e2)
# print(e2.shape)
#=======================================
# e2 = np.hstack((c,d))
# print(e2)
#=======================================
# e2 = np.vstack((c,d))
# print(e2)
#========Splitting Arrays===============

f = np.array([
    [1,2,3,4,5,5],
    [4,5,6,7,8,6],
    [3,9,2,5,8,2],
    [8,9,2,3,1,7],
])

#=======================================
# print(np.split(f,4))
# print(np.split(f,2))
#======================================
# print(np.hsplit(f,3))
#=======================================
# print(np.vsplit(f,2))
#=======================================


#=Adding Values or Adding List into array=

g = np.array([
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,5],
    [9,8,7,1]
])

h = [10,20,30,40]
#=======================================
# i = np.append(g, h)
# print(i)
#=======================================
# i = np.append(g, [h], axis=0)
# print(i)
#=======================================
# i = np.insert(g,2,h,axis=0)
# print(i)
#=======================================
# i = np.insert(g,2,h,axis=1)
# print(i)