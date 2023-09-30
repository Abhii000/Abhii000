x = int(input())
y = set(int(a) for a in input().split())
print(y)
a = int(input())

for i in range(a):
    b = input().split()
    if b[0] == 'add':
        y.add(int(b[1]))
    elif b[0] == 'remove':
        y.remove(int(b[1]))
    elif b[0] == 'discard':
        y.discard(int(b[1]))
    elif b[0] == 'pop':
        y.pop()

print(sum(y))
