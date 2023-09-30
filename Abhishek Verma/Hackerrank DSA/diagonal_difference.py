list1=[]

listA=[]
listB=[]
n=int(input())
for a in range(n):
    arr1=[int(x) for x in input().split(" ")]
    list1.append(arr1)

for i in range(n):
    for j in range(n):
        if i==j:
            listA.append(list1[i][j])
k=n-1
for x in range(n):

    listB.append(list1[x][k])
    k=k-1
print(abs(sum(listA)-sum(listB)))