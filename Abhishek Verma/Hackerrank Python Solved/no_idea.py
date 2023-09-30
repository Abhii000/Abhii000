m,n=map(int,input().split())
s1=set([int(i) for i in input().split(" ")])
list1=[]
for k in range(n):
    s2=set([int(i) for i in input().split(" ")])
    for val in s2:
        list1.append(val)
s3=set(list1)
x=s1.symmetric_difference(s3)
print(len(x))