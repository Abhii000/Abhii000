import numpy as np
while True:
    from colorama import Fore,colorama_text
    print(Fore.RED+'-----------------MATRIX MATHEMATICS----------------')
    print(Fore.CYAN+'')
    try:
        dimension=[int(input("type matrix dimension IxJ = ")) for abhi in range(2)]
        array_1 = np.array([])
        for a in range(dimension[0]):
            x=[int(a) for a in str(input()).split(" ")]
            array_1=np.append(array_1,x)
        array_1=np.reshape(array_1,(dimension[0],dimension[1]))
        print('Matrix A = ',array_1)
    except:
        print('Invalid input in Matrix A')
    #-------------------------------------------------------------------------------------------------
    try:
        print(Fore.GREEN+'\n')
        dimension2=[int(input("type = ")) for abhii in range(2)]
        array_2 = np.array([])
        for b in range(dimension[0]):
            x=[int(b) for b in str(input()).split(" ")]
            array_2=np.append(array_2,x)
        array_2=np.reshape(array_2,(dimension2[0],dimension2[1]))
        print('Matrix B = ',array_2)
        print('Type 1 for matrix multiplication\n2 for matrix addition\n3 for matrix subtraction\n4 for matrix division\n0 for close')
        while True:
            operation=input('Type operation number')
            if operation=='1':

                print('Matrix A * Matrix B = ',np.matmul(array_1,array_2))
                print('-'*80)
            elif operation=='2':
                print('Matrix A + Matrix B = ',np.add(array_1,array_2))
                print('-'*80)
            elif operation=='3':
                print('Matrix A - Matrix B = ',np.subtract(array_1,array_2))
                print('-'*80)
            elif operation=='4':
                print('Matrix A / Matrix B = ',np.divide(array_1,array_2))
                print('-'*80)
            elif operation=='0':
                break
            else:
                print('Invalid input')
    except:
        print('Invalid input in Matrix B')








