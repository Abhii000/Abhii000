import numpy as n
'''Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan'''
def solve(s):
    return ' '.join([i.capitalize() for i in s.split(' ')])
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
for a in range(1,n+1):
    print(a,end=' ')

