x=int(input())
y=[int(g)for g in input().split(" ")]
list1=[]

for m in set(y):
    for n in set(y):
        if abs(m-n)<=1:
            list1.append(m)
        else:
            continue

            
print(list1)
