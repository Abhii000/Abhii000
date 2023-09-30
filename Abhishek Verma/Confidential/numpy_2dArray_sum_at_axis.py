'''import numpy
j,k=[int(x) for x in str(input()).split()]


my_array = numpy.array([ ])

for abhi in range(j):
    b=[int(x) for x in str(input()).split()]
    numpy.append(my_array,b)
print(numpy.sum(my_array, axis =0 ))   #Output : [4 6]'''

import numpy as np

# Read the dimensions N and M
N, M = map(int, input().split())

# Read the 2D array
arr = np.array([input().split() for _ in range(N)], dtype=int)

# Calculate the sum along axis 0 (columns)
column_sum = np.sum(arr, axis=0)

# Calculate the product of the sum
result = np.prod(column_sum)

# Print the result
print(result)
