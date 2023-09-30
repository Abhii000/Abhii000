'''x=int(input())
s1=set([int(a) for a in input().split()])
n=int(input())
s2=set([int(b) for b in input().split()])

#for union
s3=s1.union(s2)
print(len(s3))

#for intersection
x=int(input())
s1=set([int(a) for a in input().split()])
n=int(input())
s2=set([int(b) for b in input().split()])
s3=s1&s2
print(len(s3))

#for difference
s3=s1.difference(s2)
print(len(s3))

#for symmetric difference
s1=set([int(a) for a in input().split()])
n=int(input())
s2=set([int(b) for b in input().split()])
s3=s1.symmetric_difference(s2)
print(len(s3))

'''
# for symmetric difference
x=int(input())
s1=set([int(a) for a in input().split()])
n=int(input())
s2=set([int(b) for b in input().split()])
print(len(s1.symmetric_difference(s2)))
