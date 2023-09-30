import time,os
import requests
os.system('cls')




def sender(src1):
    #for Sending message to telegram bot
    #start-----------------------------------------------------------------------
    k=str(input("Type the message for Client: "))
    TOKEN = '5910714156:AAEJdmAsoi6wR0MfqKMae0Ib1--xzE'
    CHAT_ID = '1309636266'
    MESSAGE = k

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': MESSAGE}
    response = requests.post(url, data=data)
    #print(response.json())
    print('Message Sent')
    print('_'*80,'\n\n')
    time.sleep(0.5)
    #end--------------------------------------------------------------------------




def reciever(src2):
    #for Recieving Messages requests from telegram bot
    #start-------------------------------------------------------------------------------
    TOKEN = '5910714156:AAEJdmAsoi6wR0MfqKMae0Ib1--xzE'
    CHAT_ID = '1309636266'
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url)
    data = response.json()
    if 'result' in data:
        for result in data['result']:
            MESSAGE = result['message']
            CHAT_ID = MESSAGE['chat']['id']
            text = MESSAGE['text']
            # do something with the message
        print('Last Message Recieved:',text)
        print('_'*80,'\n\n')
        time.sleep(0.5)
    else:
        print("No new updates")
        time.sleep(0.5)
    #end------------------------------------------------------------------------------------





def ftp(src,src3):
    TOKEN = '5910714156:AAEJdmAsoi6wR0MfqKMae0Ib1--xzE'
    CHAT_ID = '1309636266'
    #for sending File to telegram bot from computer
    #start--------------------------------------------------------------------

    #for Sending file to telegram bot
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    file_path = src
    print('Sending file...')

    with open(file_path, "rb") as f:
        response = requests.post(url, data={"chat_id": CHAT_ID}, files={"document": f})

    #print(response.status_code)
    print("Your File is sended to abhishek\n\n")
    print('_'*80,'\n\n')


    #end--------------------------------------------------------------------------
b_key=";RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/;RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/"
list7_key=list(b_key)
list5_key=[]
t_key='Zuwn9wMwZK6UUW2mvUTOtK.Ynl/ Nl3%n'
list4_key=list(t_key)

for j_key in range(0,len(list4_key)):
    list5_key.append(list7_key.index(str(list4_key[j_key])))


keygen=''

for l_key in range(0,len(list4_key)):
    keygen=str(keygen)+list7_key[list5_key[l_key]-7]
keygen2=str(keygen)+'Ib1--xzE'
print(keygen2,'...')




print('Type (send) to send message\nType (get) for get message\nType (ftp) for File Transfer\n')
while True:
    
    abhii=str(input("Listening..."))

    if abhii=='send':
        sender(keygen2)
    elif abhii=='get':
        reciever(keygen2)
    elif abhii=='ftp':
        src=str(input("Paste the file location here:"))
        ftp(src,keygen2)
    elif abhii=='close':
        break
    else:
        print("wrong input")






















