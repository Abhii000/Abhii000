import time,os,requests
from threading import Thread


box_b='test'
def reciever_live():
    global box_b

    time.sleep(0.1)
    #for Recieving Messages requests from telegram bot
    #start-------------------------------------------------------------------------------
    TOKEN = '5910714156:AAEJdmAsoi6wR0MfqKMae0iTtq0Ib1--xzE'
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url)
    data = response.json()

    message=data['result'][-1]['message']['text']
    if message in box_b:
        pass
    else:
        print(message)
        box_b=message

        
def starter_1():
    while True:
     
        reciever_live()
        time.sleep(0.1)
x_start=Thread(target=starter_1)
x_start.start()


    
    
    
    
    











