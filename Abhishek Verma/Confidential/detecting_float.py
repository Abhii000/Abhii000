'''list1=[]
for i in range(int(input())):
    k=input()
    if k.isnumeric():
        
        list1.append(int(k))
    else:
        list1.append(k)
    
for b in list1:
    if b.isfloat():
    
        print("True")
    else:
        print("False")
'''
import re

def is_valid_float(s):
    # Define a regex pattern for a valid floating-point number
    pattern = r'^[+-]?(\d*\.\d+|\d+\.\d*)([eE][+-]?\d+)?$'

    # Use the re.match function to match the pattern against the string
    if re.match(pattern, s):
        return True
    else:
        return False

# Input
n = int(input())
for _ in range(n):
    s = input()
    print(is_valid_float(s))
