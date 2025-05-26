"""
.ravel() -> it return the views of array
.flatten() -> its return the copy of the array
"""
import numpy as np

twoDimen=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDimen.flatten())

OneDimen=twoDimen.ravel()
print(OneDimen)