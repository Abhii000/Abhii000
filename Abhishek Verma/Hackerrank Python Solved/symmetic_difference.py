x=int(input())
a=set([int(i) for i in input().split(" ")])

y=int(input())
b=set([int(j) for j in input().split(" ")])

list1=[]
for abhi in sorted(a.symmetric_difference(b)):
    list1.append(abhi)
for verma in sorted(list1):
    print(verma)

#newlis = list(map(int, lis))