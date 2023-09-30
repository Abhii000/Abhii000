a=int(input())
for x in range(a):
    m=int(input())
    A = set([int(a) for a in input().split()])
    m=int(input())
    b = set([int(a) for a in input().split()])
    print(A.issubset(b))

    