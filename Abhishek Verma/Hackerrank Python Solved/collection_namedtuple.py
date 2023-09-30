x=int(input())
marks=[]
y=str(input().split(''))
print(y)
place=y.index('MARKS')
print(place)
for a in range(x+1):
    values=str(input().split(' '))
    marks.append(values[place])
sum=0
for b in marks:
    sum=sum+int(marks[b])
print