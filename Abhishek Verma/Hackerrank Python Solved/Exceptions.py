for a in range(int(input())):
    x,y=input().split(' ')
    try:
            

        
        print(int(x)//int(y))

    except Exception as e:
        print("Error Code:",e)