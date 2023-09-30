x=int(input())
y=int(input())
counter1=0
counter2=0
counter3=0
book_start=[0,1]
book_end=[0,0]
if x%2==0:
    book_end[0]=x
    book_end[1]=x+1
else:
    book_end[1]=x
    book_end[0]=x-1
#print(book_end)

while True:
    if y in book_start:
        break
    else:
        counter1+=1
        book_start[0]+=2
        book_start[1]+=2

    if y in book_end:
        break
    else:
        counter2+=1
        book_end[0]-=2
        book_end[1]-=2

if counter1<counter2:
    print(counter1)
else:
    print(counter2)