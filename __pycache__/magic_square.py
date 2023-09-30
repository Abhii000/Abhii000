
def formingMagicSquare(s):
    # List of all possible 3x3 magic squares
    magic_squares = [
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    ]

    # Calculate the cost for transforming s to each magic square
    costs = []
    for magic_square in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - magic_square[i][j])
        costs.append(cost)

    # Return the minimum cost
    return min(costs)

list1=[int(a1) for a1 in input().split(" ")]
list2=[int(a1) for a1 in input().split(" ")]
list3=[int(a1) for a1 in input().split(" ")]
# Example usage
s = []
s.append(list1)
s.append(list2)
s.append(list3)

result = formingMagicSquare(s)
print(result)  # This will output 1

'''mat=[]

list1=[int(a1) for a1 in input().split(" ")]
list2=[int(a1) for a1 in input().split(" ")]
list3=[int(a1) for a1 in input().split(" ")]
#standard magic square
sqr=[[4,9,2],
     [3,5,7],
     [8,1,6]]
counter=[]
a,b,c=list1
d,e,f=list2
g,h,i=list3
#normal-------------------------------------
if a==4:
    pass
else:
    counter.append(abs(a-4))
if b==9:
    pass
else:
    counter.append(abs(b-9))  
if c==2:
    pass
else:
    counter.append(abs(c-2))
if d==3:
    pass
else:
    counter.append(abs(d-3))
if e==5:
    pass
else:
    counter.append(abs(e-5))
if f==7:
    pass
else:
    counter.append(abs(f-7))
if g==8:
    pass
else:
    counter.append(abs(g-8))
if h==1:
    pass
else:
    counter.append(abs(h-1))
if i==6:
    pass
else:
    counter.append(abs(i-6))

mat.append(sum(counter))
counter=[]
#1st time rotated left---------------------------------
g,d,a=list1
h,e,b=list2
i,f,c=list3
if a==4:
    pass
else:
    counter.append(abs(a-4))
if b==9:
    pass
else:
    counter.append(abs(b-9))  
if c==2:
    pass
else:
    counter.append(abs(c-2))
if d==3:
    pass
else:
    counter.append(abs(d-3))
if e==5:
    pass
else:
    counter.append(abs(e-5))
if f==7:
    pass
else:
    counter.append(abs(f-7))
if g==8:
    pass
else:
    counter.append(abs(g-8))
if h==1:
    pass
else:
    counter.append(abs(h-1))
if i==6:
    pass
else:
    counter.append(abs(i-6))

mat.append(sum(counter))
counter=[]
#2nd time rotated left---------------------------------
i,h,g=list1
f,e,d=list2
c,b,a=list3
if a==4:
    pass
else:
    counter.append(abs(a-4))
if b==9:
    pass
else:
    counter.append(abs(b-9))  
if c==2:
    pass
else:
    counter.append(abs(c-2))
if d==3:
    pass
else:
    counter.append(abs(d-3))
if e==5:
    pass
else:
    counter.append(abs(e-5))
if f==7:
    pass
else:
    counter.append(abs(f-7))
if g==8:
    pass
else:
    counter.append(abs(g-8))
if h==1:
    pass
else:
    counter.append(abs(h-1))
if i==6:
    pass
else:
    counter.append(abs(i-6))

mat.append(sum(counter))
counter=[]
#3rd time rotated left---------------------------------
c,f,i=list1
b,e,h=list2
a,d,g=list3
if a==4:
    pass
else:
    counter.append(abs(a-4))
if b==9:
    pass
else:
    counter.append(abs(b-9))  
if c==2:
    pass
else:
    counter.append(abs(c-2))
if d==3:
    pass
else:
    counter.append(abs(d-3))
if e==5:
    pass
else:
    counter.append(abs(e-5))
if f==7:
    pass
else:
    counter.append(abs(f-7))
if g==8:
    pass
else:
    counter.append(abs(g-8))
if h==1:
    pass
else:
    counter.append(abs(h-1))
if i==6:
    pass
else:
    counter.append(abs(i-6))
mat.append(sum(counter))
print(min(mat))
'''