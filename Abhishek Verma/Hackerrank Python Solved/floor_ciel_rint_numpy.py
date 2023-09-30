import numpy as np

# Input
my_array = np.array(input().split(), float)

# Operations
np.set_printoptions(legacy='1.13')  # To match the expected output format
print(np.floor(my_array))
print(np.ceil(my_array))
print(np.rint(my_array))
