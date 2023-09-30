#import time,os
arr1=[]
x,y=map(int,input().split(" "))
z=[int(a) for a in input().split(" ")]
#z=[1,2,3,4,5]

    
for i in range(y):
    z.append(z[0])
    z.remove(z[0])
for abhi in z:
    print(abhi,end=" ")
    #time.sleep(0.05)
    
