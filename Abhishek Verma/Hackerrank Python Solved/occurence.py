'''Sample Input

ABCDCDC
CDC
Sample Output

2'''
import re
s = input()
k = input()
print(len(re.findall('(?=('+k+'))',s)))

