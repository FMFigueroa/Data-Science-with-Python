import numpy as np

#=========Tensor Zeros================
T_zeros = np.zeros((2,4,3))
# print(T_zeros)
#=========Tensor Ones=================
T_ones = np.ones((2,4,3))
# print(T_ones)
#=========Tensor Full=================
T_any = np.full((2,4,3), 5)
# print(T_any)
#=========Tensor Empty================
T_Empty = np.empty((2,4,3))
# print(T_Empty)
#==========Tensor Random=============
T_Random = np.random.random((2,4,3))
# print(T_Random)
#==========Vector a range============
V = np.arange(0,101,2)
# print(V)
#===========Vector linspace=========
A = np.linspace(1,10,25)
# print(A)
#==========Vector Function==========
x = np.arange(0,50,1)
y = np.sin(x)
# print(y)

#===Tensor with data type specific = Float====
T_float = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [10,20,30],
        [40,50,60]
    ]
], dtype=float)
# print(T_float)
# print(T_float.shape) # array structure
# print(T_float.size)  # number of elements
# print(T_float.ndim)  # number of dimensions or columns
# print(T_float.dtype) # data type
