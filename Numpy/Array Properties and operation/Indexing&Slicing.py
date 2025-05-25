import numpy as np

#Indexing

"""
array[index] #1d array
array[row,col] #2d array
"""

arr=np.array([1,2,3,4,5,6])
print(arr[-1])
print(arr[2])

TwoD_arr=np.array([[1,2,4],[1,2,3],[5,65,78]])
print(TwoD_arr[0,2])
print(TwoD_arr[1,2])

#Slicing

"""
array[start:stop:step]
"""
arrIn=np.array([1,2,3,4,5,6,7,8,9,10])
print(arrIn[0:9:2])
print(arr[0:5])
print(arr[:5])
print(arr[::2])
print(arr[::-1])