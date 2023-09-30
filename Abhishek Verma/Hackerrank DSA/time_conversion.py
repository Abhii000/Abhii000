x,y,z=[a for a in input().split(":")]

if 'AM' in z:
    print(f"{x}:{y}:{z[:2]}")
else:
    if x<10:

        print(f"{int(x)}:0{int(y)}:{int(z)}")
    else:
        print(f"{int(x)}:{int(y)}:{int(z)}")