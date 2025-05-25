import numpy as np

#this function is give to find the datatype of the element

arr=np.array([10,23,45,67,78])
print(arr.dtype)

#astype- it is the type of function which change the datatype of the element

arr2=np.array([1.2,3.4,66.7,99.5,76.4])
int_arr=arr2.astype(int)

print(arr2.dtype)
print(int_arr.dtype)