import numpy

def arrays(arr):
    b=numpy.array(arr,float)
    k=b[::-1]
    return k
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)