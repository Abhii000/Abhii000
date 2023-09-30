a_key=";RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/;RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/"
list1_key=list(a_key)
list2_key=[]
s_key=int(input("Type 1 for Encryption and 2 for Decryption: "))
if s_key==1:
    x_key=str(input("Type the word to encrypt = "))
    list3_key=list(x_key)

    for i_key in range(0,len(list3_key)):
        list2_key.append(list1_key.index(str(list3_key[i_key])))

    print("\n\nYour Encrypted word is = ",end="")
    for k_key in range(0,len(list3_key)):
        print(list1_key[list2_key[k_key]+7],end='')
else:
    b_key=";RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/;RmnT3b!YvcYSExA@7DzWpUo9IQFi#Ou5yPt$G1ZrHe4XwqC:%M-. J6ClkjV2KhgB&8fNLd0sa/"
    list7_key=list(b_key)
    list5_key=[]
    t_key=input("enter your decryption word = ")
    list4_key=list(t_key)

    for j_key in range(0,len(list4_key)):
        list5_key.append(list7_key.index(str(list4_key[j_key])))

    print("\n\nYour Decrypted word is = ",end="")
    for l_key in range(0,len(list4_key)):
        print(list7_key[list5_key[l_key]-7],end='')

