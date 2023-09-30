arr1=[]
array_sum=[]
for a in range(6):
    n=[int(x) for x in str(input()).split(" ")]
    arr1.append(n)
#print(arr1)

for x in range(6):
    for y in range(6):
        if x>=1 and x<=4 and y>=1 and y<=4:
            sum=arr1[x-1][y-1]+arr1[x-1][y]+arr1[x-1][y+1]
            sum1=sum+arr1[x][y]
            sum2=sum1+arr1[x+1][y-1]+arr1[x+1][y]+arr1[x+1][y+1]

            array_sum.append(sum2)
            sum=0
            sum1=0
            sum2=0
            #arr1=np.append(arr1,arr[x][y])
print(max(array_sum))


#using numpy

'''import numpy as np
arr=np.array([])
arr1=np.array([])
array_sum=np.array([])
for a in range(6):
    n=[int(x) for x in str(input()).split(" ")]

    arr=np.append(arr,np.array(n))

arr=arr.reshape(6,6)


#hourglass sum

for x in range(6):
    for y in range(6):
        if x>=1 and x<=4 and y>=1 and y<=4:
            sum=arr[x-1][y-1]+arr[x-1][y]+arr[x-1][y+1]
            sum1=sum+arr[x][y]
            sum2=sum1+arr[x+1][y-1]+arr[x+1][y]+arr[x+1][y+1]

            array_sum=np.append(array_sum,sum2)
            sum=0
            sum1=0
            sum2=0
            #arr1=np.append(arr1,arr[x][y])
array_sum=np.reshape(array_sum,(4,4))
list1=[]
for j in range(4):
    for k in range(4):
        list1.append(int(array_sum[j][k]))
print(max(list1))
    

    
#print(array_sum)'''