"""
reshape() is the function that change the shape of the array
reshaope(rows,columns) specify new shape
if dimension match
Reshaping doesn't create copy
"""
import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
Reshaped_Arr=arr.reshape(3,3)
print(Reshaped_Arr)
