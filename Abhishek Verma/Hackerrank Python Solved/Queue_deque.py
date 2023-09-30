from collections import deque
d=deque()
for a in range(int(input())):
    b=input().split()
    if b[0]=='append':
        d.append(b[1])
        print(d)
    elif b[0]=='appendleft':
        d.appendleft(b[1])
        print(d)
    elif b[0]=='pop':
        d.pop()
        print(d)
    elif b[0]=='popleft':
        d.popleft()
        print(d)

        