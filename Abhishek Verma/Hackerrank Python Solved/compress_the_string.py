x=input()
m=1
for a in range(len(x)-1):
    if x[a]==x[a+1]:
        m=m+1
        
    else:
        print(f'({m}, {x[a]})',end=' ')
        m=1
print(f'({m}, {x[a]})')
