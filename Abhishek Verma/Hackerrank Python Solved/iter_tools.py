'''You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement
s, n = input().split()
s = sorted(s)
list1=list(s)
k=list(combinations_with_replacement(list1,int(n)))
for b in k:
    print(''.join(b))
