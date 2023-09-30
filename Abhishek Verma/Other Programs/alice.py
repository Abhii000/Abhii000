try:
    print("Loading...")
    import requests,os,sys,time
    import pyttsx3,openai
    import pywhatkit
    import pyautogui
    import webbrowser
    engine = pyttsx3.init()

    import datetime

    from cmath import pi, sin
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 190)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    b=1
    c=1
    z=0
    # variable x is for person identification
    x=0
    os.system('color 03')

    def thumbnail():
        os.system('cls')
        print('\n\n\n')
        print('                                         /$$$$$$\    \$$$$$$$\                      /$$$$$$$/                    ')
        time.sleep(0.02)
        print('                                        /$$$$$$$$\    \$$$$$$$\                    /$$$$$$$/                     ') 
        time.sleep(0.02)
        print('                                       /$$$$/\$$$$\       \$$$$\                  /$$$$/                         ')
        time.sleep(0.02)
        print('                                      /$$$$/  \$$$$\       \$$$$\                /$$$$/                          ')
        time.sleep(0.02)
        print('                                     /$$$$/    \$$$$\       \$$$$\              /$$$$/                           ')
        time.sleep(0.02)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/$$$$/~~~~~~\$$$$\~~~~~~~\$$$$\~~~~~~~~~~~~/$$$$/~~~~~~~~~~~/ /~~~~~~~~~~~~~~')
        time.sleep(0.02)
        print('                                   /$$$$/        \$$$$\       \$$$$\          /$$$$/           / /               ')
        time.sleep(0.02)
        print('                   /--------------/$$$$/----------\$$$$\-------\$$$$\--------/$$$$/-----------/ /                ')
        time.sleep(0.02)
        print('                  / /------------/$$$$/------------\$$$$\-------\$$$$\------/$$$$/-------------/                 ')
        time.sleep(0.02)
        print('                 / /            /$$$$/              \$$$$\       \$$$$\    /$$$$/')
        time.sleep(0.02)
        print('~~~~~~~~~~~~~~~~/ /~~~~~~~~~~~~/$$$$/~~~~~~~~~~~~~~~~\$$$$\~~~~~~~\$$$$\~~/$$$$/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        time.sleep(0.02)
        print('                              /$$$$/                  \$$$$\       \$$$$\/$$$$/                                  ')
        time.sleep(0.02)
        print('                          /$$$$$$$/                    \$$$$$$$\    \$$$$$$$$/                                   ')
        time.sleep(0.02)
        print('                         /$$$$$$$/                      \$$$$$$$\    \$$$$$$/                                    ')
        time.sleep(0.02)
    thumbnail()

    print("Hi this is alice, show your ID to openAI module\n\nType the ID for user Verification ")
    engine.say("Type the ID for user Verification")
    engine.runAndWait()
    #Protocol Encryption 
    b_key=";RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/;RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/"
    list7=list(b_key)
    list5=[]
    t_key='3ELtb'
    list4=list(t_key)

    for j_key in range(0,len(list4)):
        list5.append(list7.index(str(list4[j_key])))
    lock=''
    for l_key in range(0,len(list4)):
        
        lock=str(lock)+list7[list5[l_key]-7]
    a=str(input(''))
    if a==lock:
        for color_delay in range(1,7):
            color_delay2='color 0'+str(color_delay)    
            os.system(color_delay2)
            time.sleep(0.02)
        os.system('color 03')

        


        
        while c<=4:
            c=c+1
            time.sleep(0.01)    
            while b<=4:
                print('Imprint Checking/',end='')
                print(b*'*')
                b=b+1
                time.sleep(0.1)
                os.system('cls')
        print('User Verified',end='')
        time.sleep(0.5)
        print('        Hello Boss. plz take the control')
        engine.say("User verified..")
        engine.runAndWait()
        l=0
        
        print('Simply type the command i am in running',end='')
        print('           /for admin commands type index   // for installing libraries type install  // for extras type extra')
        os.system('color 02')
        os.system('title Project Alice')
        while z==0:
            variable_x=1
            print('___________________________________________________________________________________________________________',datetime.datetime.now().hour,':',datetime.datetime.now().min)
            print('```````````````````````````````````````````````````````````````````````````````````````````````````````````')
            empty_que=''
            empty_ans=''
            def autosave():
                f = open("alicedata.txt", "a")
                for null_void in range(2):
                    f.write('\n')

                f.write('Question:-   ')
                f.write(empty_que)

                for null_void1 in range(2):
                    f.write('\n')
                    time.sleep(0.01)
                f.write('Answers:-')

                for null_void2 in range(2):
                    f.write('\n')
                    time.sleep(0.01)
                f.write(empty_ans)
                f.write('\n')
                f.write('----------------------------------------------------------------------------------------------')


                f.close()
                time.sleep(0.5)
                
                            
            
            alice_ai='ask me something'
            while True:
                com=str(input('\n\Listening...'))
                abhii_input=com
                


                #abhii_input=str(input('\nListening...'))
                if abhii_input=='close':
                    time.sleep(0.5)
                    print('closing...')
                    os.system('color 07')
                    time.sleep(1)
                    os.system('cls')
                    os.system('title Command Prompt')
                    z=1
                    break


                elif com=='cls':
                    os.system('cls')
                elif com=='install' or com=='pip':
                    print('Installing Requests Module')
                    os.system("pip install requests")
                    time.sleep(1)
                    os.system("color 03")
                    print("\nInstalling Text to speech\n\n")
                    time.sleep(1)
                    os.system("pip install pyttsx3")
                    time.sleep(1)
                    print("\nInstalling pywhatkit Api module\n\n")
                    time.sleep(1)
                    os.system("pip install pywhatkit")
                    os.system("color 04")
                    time.sleep(1)
                    print("done.")
                    time.sleep(1)
                    print("\nInstalling pyautogui\n\n")
                    time.sleep(1)
                    os.system("pip install pyautogui")
                    os.system("color 02")
                    time.sleep(1)
                    print("\nInstalling webbrowser api\n\n")
                    time.sleep(1)
                    os.system("pip install webbrowser")
                    os.system("color 01")
                    print("\nInstalling openai\n\n")
                    time.sleep(1)
                    os.system("pip install openai")
                    os.system("color 02")
                    time.sleep(1)
                




                elif com=='sum':
                    x=input("Type the number = ")
                    num=int(x)
                    sum=0
                    for abhi in range(0,len(x)):
                        a=num/10
                        b=int(a)
                        c=b*10
                        d=num-c
                        num=int(num/10)
                        sum=sum+d
                    print("\nThe Sum of each digit of your given no. is = ",sum)
                
                
                
                
                elif com=='whatsapp':
                    hours = datetime.datetime.now().hour
                    minutes = datetime.datetime.now().minute

                    message = str(input(("Type the message for client = ")))
                    number = input("Type the Phone number of the person = ")
                    timer=int(input("Type the time after jarvis send your message = "))
                    print(datetime.datetime.now(),"\n")


                    pywhatkit.sendwhatmsg("+91"+number,message, hours, minutes+timer,10,1)

                    print("exiting, whatsapp moodule")
                    time.sleep(1)


                elif com=='screenshot' or com=='snap' or com=='movie':
                    taker=input("movie or snap = ")
                    if taker=="movie":
                        os.system("md movie")
                        frames=int(input("Type the frames for record"))
                        abhiii=int(input("Type the time delay between each frames"))

                        for newfileabhii in range(1,frames+1):
                            myScreenshot = pyautogui.screenshot()
                            new1=str(newfileabhii)
                            myScreenshot.save('movie\\'+str(newfileabhii)+'.png')
                            time.sleep(abhiii)
                        print("all frames was taken")
                        

                    elif taker=="snap":
                        os.system("md screenshot")
                        timing=int(input("Type timer for taking screenshot = "))
                        time.sleep(timing)
                        myScreenshot = pyautogui.screenshot()
                        time.sleep(1)
                        myScreenshot.save(r'screenshot\\screenshot.png')
                        print("Done!")
                        os.startfile(r'screenshot')
                    else:
                        print("Syntax error!")
                elif com=='reverse' or com=='palindrome':
                    xmas=str(input("Type the word to reverse = "))
                    listx=[]
                    listy=[]
                    for abhii in range(0,len(xmas)):
                        listx.append(xmas[abhii])
                    for brain in range(len(xmas)-1,0,-1):
                        print(listx[brain],end="")
                        listy.append(xmas[brain])
                    listy.append(xmas[0])	
                    print(xmas[0])
                    if listx==listy:
                        print("palindrome obtained")
                    else:
                        print("not a palindrome ")
                elif com=='game':
                    n=0
                    abhii=["-","-","-","-","-","-","-","-","-"]
                    print("The TicTacToe game\n\n  Value      position\n")
                    print(abhii[0],"|",abhii[1],"|",abhii[2],"   ",1,"|",2,"|",3)
                    print(abhii[3],"|",abhii[4],"|",abhii[5]," = ",4,"|",5,"|",6)
                    print(abhii[6],"|",abhii[7],"|",abhii[8],"   ",7,"|",8,"|",3)
                    print("\nPerson1 = X\nPerson2 = O")
                    def mainbody():
                        os.system("clear")
                        print(abhii[0],"|",abhii[1],"|",abhii[2])
                        print(abhii[3],"|",abhii[4],"|",abhii[5])
                        print(abhii[6],"|",abhii[7],"|",abhii[8])
                    person1=str(input("Type person A name: "))
                    person2=str(input("Type person B name: "))
                    while True:
                        n=n+1
                        os.system("color 03")
                        print("\nPerson A Turn:")
                        print(person1, end="")
                        y=int(input(" type the position of your value = "))
                        #memory management 1
                        if y==1:
                            abhii[0]="X"
                        elif y==2:
                            abhii[1]="X"
                        elif y==3:
                            abhii[2]="X"
                        elif y==4:
                            abhii[3]="X"
                        elif y==5:
                            abhii[4]="X"
                        elif y==6:
                            abhii[5]="X"
                        elif y==7:
                            abhii[6]="X"
                        elif y==8:
                            abhii[7]="X"
                        elif y==9:
                            abhii[8]="X"
                        if abhii[0]=="X" and abhii[1]=="X" and abhii[2]=="X":
                            mainbody()
                            print("Hurray! ",person1," is Won.")
                            break
                        elif abhii[3]=="X" and abhii[4]=="X" and abhii[5]=="X":
                            mainbody()
                            print("Hurray! ",person1," is Won.")
                            break
                        elif abhii[6]=="X" and abhii[7]=="X" and abhii[8]=="X":
                            mainbody()
                            print("Hurray! ",person1," is Won.")
                            break
                        elif abhii[0]=="X" and abhii[3]=="X" and abhii[6]=="X":
                            mainbody()
                            print("Hurray! ",person1," is Won.")
                            break
                        elif abhii[1]=="X" and abhii[4]=="X" and abhii[7]=="X":
                            mainbody()
                            print("Hurray! ",person1," is Won.")
                            break
                        elif abhii[2]=="X" and abhii[5]=="X" and abhii[8]=="X":
                            mainbody()
                            print("Hurray! ",person1," is Won.")
                            break
                            
                        elif abhii[0]=="X" and abhii[4]=="X" and abhii[8]=="X":
                            mainbody()
                            print("Hurray! ",person1," is Won.")
                            break
                        elif abhii[2]=="X" and abhii[4]=="X" and abhii[6]=="X":
                            mainbody()
                            print("Hurray! ",person1," is Won.")
                            break	
                        else:
                            mainbody()
                    
                        os.system("color 06")
                        print("\nPerson B Turn:")
                        print(person2, end="")
                        n=int(input(" type the position of your value = "))
                        #memory management 2
                        if n==1:
                            abhii[0]="O"
                        elif n==2:
                            abhii[1]="O"
                        elif n==3:
                            abhii[2]="O"
                        elif n==4:
                            abhii[3]="O"
                        elif n==5:
                            abhii[4]="O"
                        elif n==6:
                            abhii[5]="O"
                        elif n==7:
                            abhii[6]="O"
                        elif n==8:
                            abhii[7]="O"
                        elif n==9:
                            abhii[8]="O"
                        if abhii[0]=="O" and abhii[1]=="O" and abhii[2]=="O":
                            mainbody()
                            print("Hurray! ",person2," is Won.")
                            break
                        elif abhii[3]=="O" and abhii[4]=="O" and abhii[5]=="O":
                            mainbody()
                            print("Hurray! ",person2," is Won.")
                            break
                        elif abhii[6]=="O" and abhii[7]=="O" and abhii[8]=="O":
                            mainbody()
                            print("Hurray! ",person2," is Won.")
                            break
                        elif abhii[0]=="O" and abhii[3]=="O" and abhii[6]=="O":
                            mainbody()
                            print("Hurray! ",person2," is Won.")
                            break
                        elif abhii[1]=="O" and abhii[4]=="O" and abhii[7]=="O":
                            mainbody()
                            print("Hurray! ",person2," is Won.")
                            break
                        elif abhii[2]=="O" and abhii[5]=="O" and abhii[8]=="O":
                            mainbody()
                            print("Hurray! ",person2," is Won.")
                            break
                            
                        elif abhii[0]=="O" and abhii[4]=="O" and abhii[8]=="O":
                            mainbody()
                            print("Hurray! ",person2," is Won.")
                            break
                        elif abhii[2]=="O" and abhii[4]=="O" and abhii[6]=="O":
                            mainbody()
                            print("Hurray! ",person2," is Won.")
                            break	
                        else:
                            mainbody()
                elif com=='blue':
                    print('thinking...\n')
                    time.sleep(0.5)
                    os.system('color 03')

                elif com=='yellow':
                    print('thinking...\n')
                    time.sleep(0.5)
                    os.system('color 06')
                
                elif com=='white':
                    print('thinking...\n')
                    time.sleep(0.5)
                    os.system('color 07')
            
                elif com=='grey':
                    print('thinking...\n')
                    time.sleep(0.5)
                    os.system('color 08')
                
                elif com=='hi':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('ohh, Hi')
                    engine.say("ohh, Hi")
                    engine.runAndWait()
                    l=1
                elif com=='hey':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('yes')
                    engine.say("yes")
                    engine.runAndWait()
                    l=1
                elif com=='hey alice':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('hello, how are you?')
                    engine.say("hello, how are you?")
                    engine.runAndWait()
                    l=1
                
                elif com=='how are you':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('i am good sir and you?')
                    engine.say("i am good sir and you?")
                    engine.runAndWait()
                    l=1
                elif com=='how are you alice':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('i am fine sir, and you?')
                    engine.say("i am fine sir, and you?")
                    engine.runAndWait()
                    
                    l=1
                elif com=='i am good':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('very well then.')
                    engine.say("very well then.")
                    engine.runAndWait()
                    
                    l=1
                
                    l=1





                elif com=='i am fine':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('very well then.')
                    engine.say("very well then.")
                    engine.runAndWait()
                    l=1
                elif com=='fine':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('very well then.')
                    engine.say("very well then.")
                    engine.runAndWait()
                    l=1
                elif com=='nice to meet you':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('nice to meet you too sir')
                    engine.say("nice to meet you too sir")
                    engine.runAndWait()
                    l=1

                #for colors modification
                
                    l=1
                elif com=='can you change the color':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('Yess, Offcourse just type the color name')
                    engine.say("Yess, Offcourse just type the color name")
                    engine.runAndWait()
                
                
                elif com=='deepblue':
                    print('thinking...\n')
                    time.sleep(0.5)
                    os.system('color 01')
                
                elif com=='green':
                    print('thinking...\n')
                    time.sleep(0.5)
                    os.system('color 02')
                
                elif com=='cyan':
                    print('thinking...\n')
                    time.sleep(0.5)
                    os.system('color 03')
                
                elif com=='red':
                    print('thinking...\n')
                    time.sleep(0.5)
                    os.system('color 04')
            
                elif com=='pink':
                    print('thinking...\n')
                    time.sleep(0.5)
                    os.system('color 05')
        
                elif com=='default':
                    print('thinking...\n')
                    time.sleep(0.5)
                    os.system('cls')
                    os.system('color 02')
                    os.system('title Project Alice')
        
                elif com=='reset':
                    print('thinking...\n')
                    time.sleep(0.5)
                    os.system('cls')
                    os.system('color 02')
                    os.system('title Project Alice')

                elif com=='home':
                    print('thinking...\n')
                    time.sleep(0.5)
                    os.system('cls')
                    os.system('color 02')
                    os.system('title Project Alice')
                    
                

                elif com=='who made you':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('name is abhii')
                    engine.say("name is abhii")
                    engine.runAndWait()

                
                elif com=='really':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('yess')
                    engine.say("yess")
                    engine.runAndWait()
        
                elif com=='haha':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('you laughing')
                    engine.say("you laughing ")
                    engine.runAndWait()
            
                elif com=='i am abhii':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('helo boss')
                    engine.say("helo boss")
                    engine.runAndWait()
        
                elif com=='i am abhishek':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('helo boss')
                    engine.say("helo boss")
                    engine.runAndWait()
        
                elif com=='my name is abhi':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('helo boss')
                    engine.say("helo boss")
                    engine.runAndWait()
        
                elif com=='my name is abhishek':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('helo boss')
                    engine.say("helo boss")
                    engine.runAndWait()
        
                
                elif com=='who is your boss':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('my boss is not exist but. i am well designed and operated by Abhishek Verma')
                
            
                
                
                elif com=='':
                    print('say something')
        
                elif com=='what is your name':
                    print('thinking...\n')
                    time.sleep(0.5)
                    
                    if x==0:
                        naam=input('i am Alice. What is your name? ')
                        print('Nice to meet you',naam)
                        engine.say("Nice to meet you"+naam)
                        engine.runAndWait()
                        x=1
                        l=1
                    else: print('Already told.')
                    engine.say("Already told.")
                    engine.runAndWait()
            
                    
                elif com=='what are you doing':
                    time.sleep(0.5)
                    print('I think, i am talking to you.')
                    
        
                elif com=='you are cute':
                
                    time.sleep(0.5)
                    print('yes i am:)')
            
                elif com=='you are good':
                
                    time.sleep(0.5)
                    print('yes i am:)')
                
            
                elif com=='are you girl':
                
                    time.sleep(0.5)
                    print('yess :)')
                
                
                elif com=='are you a girl':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('off course:)')
                
                
                elif com=='i like you':
                    print('thinking...\n')
                    time.sleep(0.5)
                    print('I like you too')
                
            
                elif com=='open website':
                    web=input('just type the website name only')
                    os.system('start chrome ' +web+'.com')
                    time.sleep(0.5)
                
                elif com=='open dir':
                    dir=input('type the command')
                    os.system('dir')
                    time.sleep(2)
                
                elif com=='show me ip':
                    dir=input('type the command')
                    os.system('ipconfig')
                    time.sleep(0.5)
                
                




                    
                elif com=='call':
                    os.system('call')
                    time.sleep(0.5)
            
                elif com=='cd':
                    os.system('cd')
                    time.sleep(0.5)
            
                elif com=='cls':
                    os.system('cls')
                    time.sleep(0.5)
                
                elif com=='color':
                    os.system('color')
                    time.sleep(0.5)
            
                elif com=='date':
                    os.system('date')
                    time.sleep(0.5)
            
                elif com=='dir':
                    os.system('dir')
                    time.sleep(0.5)
            
                elif com=='echo':
                    os.system('echo')
                    time.sleep(0.5)
                
                elif com=='exit':
                    os.system('exit')
                    time.sleep(0.5)
            
                elif com=='find':
                    os.system('find')
                    time.sleep(0.5)
                
                elif com=='hostname':
                    os.system('hostname')
                    time.sleep(0.5)
                
                elif com=='pause':
                    os.system('pause')
                    time.sleep(0.5)
            
                elif com=='runas':
                    os.system('runas')
                    time.sleep(0.5)
                
                elif com=='sort':
                    os.system('sort')
                    time.sleep(0.5)
                
                elif com=='start':
                    os.system('start')
                    time.sleep(0.5)
                
                elif com=='taskkill':
                    os.system('taskkill')
                    time.sleep(0.5)
                
                elif com=='tasklist':
                    os.system('tasklist')
                    time.sleep(0.5)
                
                elif com=='time':
                    os.system('time')
                    time.sleep(0.5)
                
                elif com=='timeout':
                    os.system('timeout')
                    time.sleep(0.5)
            
                elif com=='title':
                    ox=input('type the title name = ')
                    os.system('title '+ox)
                    time.sleep(0.5)
            
                elif com=='ver':
                    os.system('ver')
                    time.sleep(0.5)
            
                elif com=='w32tm':
                    os.system('w32tm')
                    time.sleep(0.5)
            
                elif com=='ftp':
                    os.system('ftp')
                    time.sleep(0.5)
                    
                elif com=='ftype':
                    os.system('ftype')
                    time.sleep(0.5)
                    
                elif com=='getmac':
                    os.system('getmac')
                    time.sleep(0.5)
                
                elif com=='mac':
                    os.system('getmac')
                    time.sleep(0.5)
                    
                elif com=='ip':
                    os.system('ipconfig')
                    time.sleep(0.5)
                    
                elif com=='ipconfig':
                    os.system('ipconfig')
                    time.sleep(0.5)
                
                elif com=='netsh':
                    os.system('netsh')
                    time.sleep(0.5)
                
                elif com=='netstat':
                    os.system('netstat')
                    time.sleep(0.5)
                
                elif com=='netinfo':
                    os.system('netstat')
                    time.sleep(0.5)
            
                elif com=='nslookup':
                    os.system('nslookup')
                    time.sleep(0.5)
                    
                elif com=='pathping':
                    os.system('pathping')
                    time.sleep(0.5)
                
                elif com=='ping':
                    os.system('ping')
                    time.sleep(0.5)
                
                elif com=='route':
                    os.system('route')
                    time.sleep(0.5)
                
                elif com=='route print':
                    os.system('route print')
                    time.sleep(0.5)
                
                elif com=='systeminfo':
                    os.system('systeminfo')
                    time.sleep(0.5)
                
                elif com=='info':
                    os.system('systeminfo')
                    time.sleep(0.5)
                    
                elif com=='telnet':
                    os.system('telnet')
                    time.sleep(0.5)
                    
                elif com=='tftp':
                    os.system('tftp')
                    time.sleep(0.5)
                    
                elif com=='attrib':
                    os.system('attrib')
                    time.sleep(0.5)
                
                elif com=='comp':
                    os.system('comp')
                    time.sleep(0.5)
                
                elif com=='compact':
                    os.system('compact')
                    time.sleep(0.5)
                
                elif com=='copy':
                    os.system('copy')
                    time.sleep(0.5)
                
                elif com=='xcopy':
                    os.system('xcopy')
                    time.sleep(0.5)
                    
                elif com=='diskcomp':
                    os.system('diskcomp')
                    time.sleep(0.5)
                
                elif com=='diskcopy':
                    os.system('diskcopy')
                    time.sleep(0.5)
                    
                elif com=='erase':
                    os.system('erase')
                    time.sleep(0.5)
                
                elif com=='del':
                    os.system('del')
                    time.sleep(0.5)
                    
                elif com=='expand':
                    os.system('expand')
                    time.sleep(0.5)
                
                elif com=='fc':
                    os.system('fc')
                    time.sleep(0.5)
                
                elif com=='mkdir':
                    os.system('mkdir')
                    time.sleep(0.5)
                
                elif com=='move':
                    os.system('move')
                    time.sleep(0.5)
                    
                elif com=='rename':
                    os.system('rename')
                    time.sleep(0.5)
                
                elif com=='replace':
                    os.system('replace')
                    time.sleep(0.5)
                
                elif com=='rmdir':
                    os.system('rmdir')
                    time.sleep(0.5)
                
                elif com=='rd':
                    os.system('rd')
                    time.sleep(0.5)
                    
                elif com=='tree':
                    os.system('tree')
                    time.sleep(0.5)
                    
                elif com=='type':
                    os.system('type')
                    time.sleep(0.5)
                    
                elif com=='chkdsk':
                    os.system('chkdsk')
                    time.sleep(0.5)
                    
                elif com=='chkntfs':
                    os.system('chkntfs')
                    time.sleep(0.5)
                
                elif com=='defrag':
                    os.system('defrag')
                    time.sleep(0.5)
                
                elif com=='diskpart':
                    os.system('diskpart')
                    time.sleep(0.5)
                
                elif com=='driverquery':
                    os.system('driverquery')
                    time.sleep(0.5)
                
                elif com=='label':
                    os.system('label')
                    time.sleep(0.5)
                    
                elif com=='mode':
                    os.system('mode')
                    time.sleep(0.5)
                
                elif com=='mountvol':
                    os.system('mountvol')
                    time.sleep(0.5)
                    
                elif com=='verify':
                    os.system('verify')
                    time.sleep(0.5)
            
                elif com=='vol':
                    os.system('')
                    time.sleep(0.5)
                    
                elif com=='for':
                    os.system('for')
                    time.sleep(0.5)
                
                elif com=='gpresult':
                    os.system('gpresult')
                    time.sleep(0.5)
                    
                elif com=='gpupdate':
                    os.system('gpupdate')
                    time.sleep(0.5)
                
                elif com=='perfmon':
                    os.system('perfmon')
                    time.sleep(0.5)
                
                elif com=='invert':
                    os.system('color 70')
                    
                elif com=='location':
                    print(os.getcwd())
                    
                    k=os.getcwd()
                    folder_path = r"{}"
                    n=folder_path.format(k)
                    os.startfile(n)
                    time.sleep(0.5)
                    

                elif com=='extra':
                    print("There are some extra simple codes added for just for testing purpose\n")
                    print("pip\nadmin\nwhatsapp\nsum\nreverse\ngame\nsnap\nscreenshot\nmovie\ncolor name\ngcd\nphysics\nastro date\nupdate\nwebsite\nlocation\npalindrome\nloop\nloop1\nloop2")
                
                elif com=='update':
                    print("Download the latest alice version from google drive.")
                    url1= 'https://drive.google.com/drive/folders/1lLKMS8VdnzT6uMNfa8ipiCUILTvOod6-'
                    webbrowser.open_new_tab(url1)
                    
                elif com=='website':
                    print("Opening website")
                    url2= 'https://abhi639679.wixsite.com/abhishek'
                    webbrowser.open_new_tab(url2)
                




                elif com=='prompt':
                    os.system('prompt')
                    time.sleep(0.5)
                
                elif com=='disco':
                    #color changer program
                    ana=0
                    bela=0
                    speeder=float(input("type the frequency of lights(in milliseconds) = "))
                    os.system("color 02")
                    while True:
                        os.system("color "+str(bela))
                        bela=bela+1
                        time.sleep(speeder)
                        if bela==10:
                            bela=1
                            while ana>=1:
                                os.system("color "+str(bela))
                                bela=bela-1
                                time.sleep(speeder)
                

                    time.sleep(0.5)
                
                elif com=='gcd':
                    #find greatest common divisor of both number+
                    valuea=int(input("type the 1st number"))
                    valueb=int(input("type the 2nd number"))
                    man=valuea
                    nan=valueb
                    ikey=1
                    jkey=1
                    xlist=[]
                    ylist=[]
                    zlist=[]
                    for ikey in range(1,valuea):
                        ikey=ikey+1
                        if valuea%ikey==0:
                            xlist.append(ikey)
                    for jkey in range(1,valueb):
                        jkey=jkey+1
                        if valueb%jkey==0:
                            ylist.append(jkey)

                    print("Factors of",man," = ",xlist)
                    print("Factors of",nan," = ",ylist)
                    sam=max(xlist)
                    tam=max(ylist)
                    for abhi in xlist:
                        if abhi in ylist:
                            zlist.append(abhi)
                    print("Intersection Between Both No. is = ", zlist)
                    print("So Grteatest Common Divisor is = ", max(zlist))



                    '''
                    a=[int(input('first:')),int(input('second:'))]
                    c=[x for x in range(2,a[0]) if a[0]%x==0]
                    d=[x for x in range(2,a[1]) if a[1]%x==0]
                    z=max([a for a in c if a in d])
                    '''

                    time.sleep(0.5)
                    

                elif com=='i am abhi':
                    thumbnail()
                    
                
                elif com=='loop2':
                    r=1
                    s=0
                    c=r
                    while True:


                        while s==0:
                            print('---',r/10,'-----      -----',r,'-----------------')
                            r=r*10
                            time.sleep(0.01)
                            if r==10000000000:
                                s=1 
                        while s==1:

                            print('---',r/10,'-----     ------',r,'-----------------')
                            r=r/10
                            time.sleep(0.01)
                            if r==1:
                                s=0
                    

                elif com=='loop1':
                    a=10
                    b=20
                    c=25

                    while a<=40:
                        print(c*' ',end='')
                        print(a*'*')
                        a=a+2
                        b=b+1
                        c=c-1
                        time.sleep(0.01)

                        if a==40:
                            while a>=3:
                                print(c*' ',end='')
                                print(a*'*')
                                a=a-2
                                b=b-1
                                c=c+1
                                time.sleep(0.01)
                
                elif com=='loop':
                    abhii=10
                    k=1
                    while k<=abhii:
                        for a in range(1,abhii):
                                k=k+2
                                print(" "*10,"HH"," "*10,"##"," "*10,"HH",end="")
                                print("-"*a,"*"*a,"*"*k)
                                time.sleep(0.02)
                                if a==abhii-1:
                                            for b in range(1,abhii):
                                                a=a-1
                                                k=k-2
                                                print(" "*10,"HH"," "*10,"  "," "*10,"HH",end="")
                                                print("A"*a,"*"*a,"*"*k)
                                                
                                                time.sleep(0.02)

                
                #wifi password finder
                elif com=='wifi':
                    os.system('netsh wlan show profile')
                    wifi=input('type the wifi name from user profiles.(case Sensitive)')
                    print('Check key content in security settings = wifi password')
                    time.sleep(3)
                    os.system('netsh wlan show profile '+wifi+' key=clear')

                    time.sleep(0.5)
                
                #main admin codes run in cmd
                
                
                
                elif com=='admin':
                    os.system('cls')
                    os.system('color 03')

                    def sender(abhii,verma):
                        #for Sending message to telegram bot
                        #start-----------------------------------------------------------------------
                        time.sleep(0.1)
                        k=str(input("Type the message for Client: "))
                        TOKEN = abhii
                        CHAT_ID = verma
                        MESSAGE = k

                        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
                        data = {'chat_id': CHAT_ID, 'text': MESSAGE}
                        response = requests.post(url, data=data)
                        #print(response.json())
                        print('Message Sent')
                        print('_'*80,'\n\n')
                        time.sleep(0.5)
                        #end--------------------------------------------------------------------------




                    def reciever(abhi1,verma1):
                        time.sleep(0.1)
                        #for Recieving Messages requests from telegram bot
                        #start-------------------------------------------------------------------------------
                        TOKEN = abhi1
                        CHAT_ID = verma1
                        url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
                        response = requests.get(url)
                        data = response.json()
                        if 'result' in data:
                            for result in data['result']:
                                
                                MESSAGE = result['message']
                                CHAT_ID = MESSAGE['chat']['id']
                                text = MESSAGE['text']
                                # do something with the message
                            try:
                                print('Last Message Recieved:',text)
                            except:
                                print('Not yet any message recieved')
                            print('_'*80,'\n\n')
                            time.sleep(0.5)
                        else:
                            print("No new updates")
                            time.sleep(0.5)
                        #end------------------------------------------------------------------------------------

                    def ftp(src,abhi2,verma2):
                        time.sleep(0.1)
                        TOKEN = abhi2
                        CHAT_ID = verma2
                        #for sending File to telegram bot from computer
                        #start--------------------------------------------------------------------

                        #for Sending file to telegram bot
                        url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
                        file_path = src
                        print('Sending file...')

                        with open(file_path, "rb") as f:
                            response = requests.post(url, data={"chat_id": CHAT_ID}, files={"document": f})

                        #print(response.status_code)
                        print("Your File is sended to the developer\n\n")
                        print('_'*80,'\n\n')


                        #end--------------------------------------------------------------------------
                    rule_book1=''
                    rule_book2=''
                    #encryption protocol1
                    b_key=";RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/;RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/"
                    list7_key=list(b_key)
                    list5_key=[]
                    t_key='Zuwn9wMwZK6UUW2mvUTOtK.Ynl'
                    list4_key=list(t_key)

                    for j_key in range(0,len(list4_key)):
                        list5_key.append(list7_key.index(str(list4_key[j_key])))
                    keygen=''
                    #print("\n\nYour Decrypted word is = ",end="")
                    for l_key in range(0,len(list4_key)):
                        keygen=keygen+str(list7_key[list5_key[l_key]-7])
                    keygen2=keygen+'fqKMae0iTtq0Ib1--xzE'

                    #encryption protocol2
                    b_key1=";RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/;RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/"
                    list7_key1=list(b_key1)
                    list5_key1=[]
                    t_key1='wSnuKSKfKK'
                    list4_key1=list(t_key1)

                    for j_key1 in range(0,len(list4_key1)):
                        list5_key1.append(list7_key1.index(str(list4_key1[j_key1])))
                    keygen1=''
                    #print("\n\nYour Decrypted word is = ",end="")
                    for l_key1 in range(0,len(list4_key1)):
                        keygen1=keygen1+str(list7_key1[list5_key1[l_key1]-7])
                    keygen3=keygen1

                    print('This Section is for Developer\n')
                    url3= 'https://t.me/V_Alice_bot'

                    print('Type (send) to send message\nType (get) for get message\nType (ftp) for File Transfer\nType (open) for open bot domain ')

                    while True:
                        
                        abhii=str(input("\nabhishek:\metaserver\Listening..."))

                        if abhii=='send':
                            sender(keygen2,keygen3)
                        elif abhii=='get':
                            reciever(keygen2,keygen3)
                        elif abhii=='ftp':
                            k=os.getcwd()
                            folder_path = r"{}"
                            n=folder_path.format(k)
                            os.startfile(n)
                            time.sleep(0.5)
                            src=str(input("Paste the file location here:"))
                            ftp(src,keygen2,keygen3)
                        elif abhii=='open':
                            webbrowser.open_new_tab(url3)
                            print('\n')

                        elif abhii=='close'or'exit':
                            os.system('cls')
                            os.system('color 02')
                            os.system('color 02')
                            break
                        else:
                            print("wrong input")
                            os.system('color 02')


                
                elif com=='control panel':
                    os.system('ncpa.cpl')
                    time.sleep(0.5)
                
                elif com=='ncpa.cpl':
                    os.system('ncpa.cpl')
                    time.sleep(0.5)
                    
                elif com=='network properties':
                    os.system('ncpa.cpl')
                    time.sleep(0.5)
                
                elif com=='adapter settings':
                    os.system('ncpa.cpl')
                    time.sleep(0.5)
                
                elif com=='network':
                    os.system('wmic nic get name, index')
                    time.sleep(0.5)
                    
                elif com=='dns':
                    os.system('nslookup')
                    time.sleep(0.5)
                
                elif com=='dns lookup':
                    os.system('nslookup')
                    time.sleep(0.5)
                    
                
                elif com=='tracert':
                    ser=input('Type the dns IP etc 8.8.8.8 OR website name')
                    os.system('tracert '+ser)
                    time.sleep(0.5)
                
                elif com=='arp':
                    os.system('arp')
                    time.sleep(0.5)
                
                elif com=='arp -a':
                    os.system('arp -a')
                    time.sleep(0.5)
                
                elif com=='speak':
                    engine.say(alice_ai)
                    engine.runAndWait()
                    
                    





                elif com=='shutdown':
                    dir=input('yes/no')
                    if dir=='yes':
                        os.system('shutdown/s')
                        print('shutting down the system')
                    else: time.sleep(0.5)
                
                elif com=='index':
                    
                    print('_'*26)
                    time.sleep(0.03)
                    print('DEVELOPER: ABHISHEK VERMA \\')
                    time.sleep(0.03)
                    print('PROJECT ALICE VERSION-3.6  \\'+'_'*128)
                    time.sleep(0.03)
                    print('````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````')
                    time.sleep(0.01)
                    print('attrib      = display file attributes',end='')

                    time.sleep(0.01)
                    print('                         pause       = pauses the execution of a batch file and shows a message')
                    
                    print('call        = calls a batch file from another one',end='')
                    time.sleep(0.01)
                    print('             pause       = pauses the execution of a batch file and shows a message')
                    

                    print('cd          = change directory',end='')
                    time.sleep(0.01)
                    print('                                runas       = start a program as another user')
                    
                    
                    print('cls         = clear screen',end='')
                    time.sleep(0.01)
                    print('                                    rmdir / rd  = delete directory')
                    

                    print('cmd         = start command prompt',end='')
                    time.sleep(0.01)
                    print('                            replace     = replace files')
                    

                    print('copy/xcopy  = copy files',end='')
                    time.sleep(0.01)
                    print('                                      rename      = rename files')
                    

                    print('compact     = display/change file compression',end='')
                    time.sleep(0.01)
                    print('                 reg         = add/read/import/export registry entries')
                
                    print('comp        = compare file contents',end='')
                    time.sleep(0.01)
                    print('                           route       = display network routing table, add static routes/type route print for print')
                

                    print('chkntfs     = display/change volume check at startup',end='')
                    time.sleep(0.01)
                    print('          shutdown    = shutdown the computer')
                    

                    print('chkdsk      = check volumes',end='')
                    time.sleep(0.01)
                    print('                                   sort        = sort the screen output')
                    

                                

                    print('driverquery = display installed devices and their properties',end='')
                    time.sleep(0.01)
                    print('  systeminfo  = displays computer-specific properties and configurations')
                    

                    print('diskpart    = volume management',end='')
                    time.sleep(0.01)
                    print('                               tracert     = trace routes similar to patchping')
                    

                    print('defrag      = defragment media',end='')
                    time.sleep(0.01)
                    print('                                taskkill    = terminate a process or a application')
                    

                    print('diskcopy    = copy floppy disc to another one',end='')
                    time.sleep(0.01)
                    print('                 tasklist    = display applications and related task')
                

                    print('diskcomp    = compare content of two floppy disks',end='')
                    time.sleep(0.01)
                    print('             time        = display/edit the system time')
                    

                    print('dir         = list directory content',end='')
                    time.sleep(0.01)
                    print('                          timeout     = wait any time')
                

                    print('echo        = text output',end='')
                    time.sleep(0.01)
                    print('                                     title       = set title for prompt')
                    

                    print('expand      = extract files',end='')
                    time.sleep(0.01)
                    print('                                   type        = display content of text files')
                    

                    print('erase / del = delete one or more files',end='')
                    time.sleep(0.01)
                    print('                        tree        = display folder structure graphically')
                    

                    print('exit        = exits the command prompt or a batch file',end='')
                    time.sleep(0.01)
                    print('        tftp        = transfer files to a TFTP server')
                    

                    print('find        = find files',end='')
                    time.sleep(0.01)
                    print('                                      telnet      = establish Telnet connection')
                    

                    print('format      = format volumes',end='')
                    time.sleep(0.01)
                    print('                                  ver         = display operating system version')
                    

                    print('ftp         = transfer files to a FTP server',end='')
                    time.sleep(0.01)
                    print('                  verify      = monitoring whether volumes are written correctly')
                    

                    print('fc          = copare files and display the differences',end='')
                    time.sleep(0.01)
                    print('        vol         = show volume description and serial numbers of the HDDs')
                    

                    print('ftype       = display file type and mapping',end='')
                    time.sleep(0.01)
                    print('                   w32tm       = setting time synchronisation/time server/time zone')
                    

                    print('for         = for loop',end='')
                    time.sleep(0.01)
                    print('                                        move        = move/rename files')
                

                    print('gpresult    = display group policies',end='')
                    time.sleep(0.01)
                    print('                          mkdir       = create a new directory')
                

                    print('getmac      = display MAC address',end='')
                    time.sleep(0.01)
                    print('                             netsh       = configure/control/display network components')
                    
                    print('gpupdate    = update group policies',end='')
                    time.sleep(0.01)
                    print('                           netstat     = display TCP/IP connections and status')
                    
                    print('hostname    = display host name',end='')
                    time.sleep(0.01)
                    print('                               nslookup    = query the DNS')
                    

                    print('ipconfig    = display IP network settings',end='')
                    time.sleep(0.01)
                    print('                     pathping    = test the connection to a specific IP address')
                

                    print('label       = change volume name',end='')
                    time.sleep(0.01)
                    print('                              ping        = pings the network')
                


                    print('mountvol    = assign/delete drive mountpoints',end='')
                    time.sleep(0.01)
                    print('                 perfmon     = start performance monitor')
                

                    print('mode        = configure interfaces/devices',end='')
                    time.sleep(0.01)
                    print('                    prompt      = change command prompt')
                    
                    print('ncpa.cpl    = To open adapter properties',end='')
                    time.sleep(0.01)
                    print('                      network     = show all network adapters')
                    
                    print('nslookup    = for Dns Lookup & server IP check',end='')
                    time.sleep(0.01)
                    print('                wifi        = for checking wifi passwords')

                    print('tracert     = tracing the IP and Ping of website ',end='')
                    time.sleep(0.01)
                    print('             arp /arp -a = it will show you the table ARP Poisioning')
                
                    

                
                    
                else:

                    try:
                    
                        print('thinking...\n\n')
                        

                        os.environ["OPENAI_API_KEY"] = "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"
                        openai.api_key = os.getenv("OPENAI_API_KEY")
                        response = openai.Completion.create(
                            model="text-davinci-003",
                            prompt="Q:"+abhii_input+"\nA:",
                            temperature=1,
                            max_tokens=2000,
                            top_p=1,
                            frequency_penalty=0.0,
                            presence_penalty=0.0,
                            stop=["A:"]
                        )
                        alice_ai=response['choices'][0]['text']
                        empty_ans=alice_ai
                        empty_que=abhii_input


                        #print('\n\n',variable_x)


                        text_lines=alice_ai.splitlines()
                        
                        for variable1 in range(0,len(text_lines)):
                            print(text_lines[variable1])
                            time.sleep(0.1)
                        autosave()


                        #engine.say(alice_ai)
                        #engine.runAndWait()
                        print('\n\n======================================================================================================================')
                    except:
                        print('Connection interrupted due to Data-Packets Lost. check your internet connection. try again')
                        
                    
                
                
        
    else: 
        os.system('color 04')
        os.system('cls') 
        if z==0:
            
            print('Unauthorised access!')
            engine.say(" Unauthorised access!")
            engine.runAndWait()
            
            
            time.sleep(1)
            os.system('cls')
            print('\nClosing the program')
            os.system('color 07')
            os.system('exit')
            
        else:
            print('Closing the program')
            
            os.system('exit')
except:
    
    os.system('color 07')
    print('Connection Failed. Check your internet connection!')
    time.sleep(3)
    os.system('cls')
            