import numpy as np
# temperature=[22.3,55.6,27,45,34]
# total=0

# for temp in temperature:
#     total+=temp

# average=total/len(temperature)
# print(average)

temperature=np.array([22.3,55.6,27,45,34])  #one dimensional array
average=np.mean(temperature)
print(average)

twoDimen=np.array([[1,2,3],[4,5,6],[7,8,9]])  #Two Dimensional array
print(twoDimen)