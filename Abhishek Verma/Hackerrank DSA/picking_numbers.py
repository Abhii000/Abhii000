x=int(input())
list1=[]
aditya=[int(a) for a in input().split(" ")]

for a in aditya:
    for b in aditya:
        if abs(a-b)<=1:
            list1.append(a)

print(list1)
