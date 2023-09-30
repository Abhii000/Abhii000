import time,os,webbrowser,requests
a=['abhi','verma']
def reciever(abhi1,verma1):
    global a,b,text
    
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
            a.append(text)
            
           

        except:
            print('Not yet any message recieved')
        print('_'*80,'\n\n')
        time.sleep(0.5)
    else:
        print("No new updates")
        time.sleep(0.5)
    #end------------------------------------------------------------------------------------





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






while True:
    if a[len(a)-1]!=a[len(a)-2]:
        reciever(keygen2,keygen3)
        time.sleep(0.1)
    else:
        print('nope')
        time.sleep(0.1)

   