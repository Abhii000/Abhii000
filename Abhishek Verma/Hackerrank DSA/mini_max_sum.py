a=[int(a)for a in input().split(" ")]
list1=[]
for x in range(len(a)):
    t=a.copy()
    t.pop(x)
    
    list1.append(sum(t))
print(min(list1),max(list1))

'''k=0

list1=[]
x=[int(a)for a in input().split(" ")]

y=x
for i in range(len(x)):
    
    y[i]=0
    list1.append(sum(y))
    print(y)
    y=x
    
    
print(list1)

'''