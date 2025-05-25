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

MultiDimen=np.array([[[1,3],[1,4],[4,5]],[[1,3],[1,4],[4,5]]])  #three dimensional array
print(MultiDimen)

zeromatrix=np.zeros(3)  #add zero in the matrix
print(zeromatrix)

onesMatrix=np.ones((3,4)) #add ones in the matix 
print(onesMatrix)


#full(shape,value)

anyMatrix=np.full((5,6),2)
print(anyMatrix)