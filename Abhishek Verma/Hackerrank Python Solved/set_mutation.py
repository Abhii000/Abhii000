x = int(input())
s1 = set([int(a) for a in input().split()])
n = int(input())
for a in range(n):
    z = input().split()
    if z[0] == 'intersection_update':
        s1.intersection_update(set([int(a) for a in input().split()]))
    elif z[0] == 'update':
        s1.update(set([int(a) for a in input().split()]))
    elif z[0] == 'symmetric_difference_update':
        s1.symmetric_difference_update(set([int(a) for a in input().split()]))
    elif z[0] == 'difference_update':
        s1.difference_update(set([int(a) for a in input().split()]))   

print(sum(s1))
