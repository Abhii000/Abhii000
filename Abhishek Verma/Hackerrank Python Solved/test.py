#make a program to draw a square pattern using input from user
n=int(input("enter the number of rows:"))
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

#make a program to draw a triangle pattern using input from user
n=int(input("enter the number of rows:"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()



