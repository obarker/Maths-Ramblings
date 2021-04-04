import numpy as np

f_i = 100

print(type(f_i))
# <class 'float'>

#print(isinstance(f_i, int))
# False

#print(isinstance(f_i, float))
# True

arr = np.array([])
parr = np.array([])

for i in range(1,200):
    arr = np.append(arr,i)   
    print (arr[-1])
    print(isinstance(i / (arr[-1]), int))


