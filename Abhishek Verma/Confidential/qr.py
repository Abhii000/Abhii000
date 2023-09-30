import time,os
a=0

while True:
    for x in range(1,30):
        print('*'*20)
        time.sleep(0.05)
        if x==28:

            for x in range(30,1,-1):
                print('*'*20)
                time.sleep(0.05)
    