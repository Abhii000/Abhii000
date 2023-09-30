'''x,y=map(int,input().split())
list1=[]
list2=[]
for a in range(x):
    i=[int(q) for q in str(input()).split(" ")]
    list1.append(max(i))
for abhi in list1:
    list2.append(abhi**2)
print(sum(list2)%y)
'''
from itertools import product

def maximize_value(n, m, lists):
    max_value = 0

    for combination in product(*lists):
        value = sum(x**2 for x in combination) % m
        max_value = max(max_value, value)

    return max_value

# Input
n, m = map(int, input().split())
lists = [list(map(int, input().split()))[1:] for _ in range(n)]

# Calculate and print the result
result = maximize_value(n, m, lists)
print(result)
