from collections import Counter

x=int(input())
shoes_size=Counter(map(int,input().split()))
y=int(input())
income=0
for i in range(y):
    size,price=map(int,input().split())
    if shoes_size[size]:
        income+=price
        shoes_size[size]-=1

print(income)
