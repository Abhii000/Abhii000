a=[int(x) for x in input().split(" ")]
b=[int(y) for y in input().split(" ")]

alice=0
bob=0

for i in range(len(a)):
    if a[i]>b[i]:
        alice+=1
    elif a[i]<b[i]:
        bob+=1
    else:
        continue

print(alice,bob)