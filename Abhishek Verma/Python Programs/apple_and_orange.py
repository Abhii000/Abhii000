s,t=map(int,input().split(" "))
house_range=[abhi for abhi in range(s,t+1)]
a,b=map(int,input().split(" "))


apple_distance=[]
orange_distance=[]



m,n=map(int,input().split(" "))
apples=[int(x) for x in input().split(" ")]
oranges=[int(x) for x in input().split(" ")]


for dist1 in apples:
    if (dist1+a) in house_range:

        apple_distance.append(dist1+a)

for dist2 in oranges:
    if (dist2+b) in house_range:
        orange_distance.append(dist2+b)

print(len(apple_distance))
print(len(orange_distance))