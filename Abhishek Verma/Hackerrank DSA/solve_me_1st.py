list1=[]
list2=[]
x=[a for a in input().split(" ")]
y=[b for b in input().split(" ")]
for i in x:
    if i.isdigit():
        list1.append(int(i))
for j in y:
    if j.isdigit():
        list2.append(int(j))
print(int(list1[0])+int(list2[0]))