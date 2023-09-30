list1=[]
for i in range(int(input(''))):
    n=input('').split(' ')
    m=list(n)
    if m[0]=='insert':
        list1.insert(int(m[1]),int(m[2]))

    elif m[0]=='print':
        print(list1)
    elif m[0]=='remove':
        list1.remove(int(m[1]))
    elif m[0]=='append':
        list1.append(int(m[1]))
    elif m[0]=='sort':
        list1.sort()
    elif m[0]=='pop':
        list1.pop()
    elif m[0]=='reverse':
        list1.reverse()

