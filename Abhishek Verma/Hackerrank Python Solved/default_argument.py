
def odd(k):
    odd1=1
    for abhi in range(k):
        print(odd1)
        odd1=odd1+2
def even(l):
    even1=0
    for abhi1 in range(l):
        print(even1)
        even1=even1+2
for i in range(int(input())):
    z=[j for j in str(input()).split(" ")]
    if z[0]=='odd':
        odd(int(z[1]))
    elif z[0]=='even':
        even(int(z[1]))
