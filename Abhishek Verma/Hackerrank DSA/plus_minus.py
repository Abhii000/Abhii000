n=int(input())
neg=0
pos=0
zero=0

list1=[]

arr=[x for x in input().split(" ")]
for b in arr:
    if int(b)>0:
        pos+=1
    elif int(b)<0:
        neg+=1
    elif int(b)==0:
        zero+=1

print(pos/n)
print(neg/n)
print(zero/n)
