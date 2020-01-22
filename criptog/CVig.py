import os
import time
def cv():  
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    print('-=-=-=-=-=-=-=-=-=-Vigenére Cypher-=-=-=-=-=-=-=-=-=-')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    base= 'abcdefghijklmnopqrstuvwxyz'
    w=0
    row = []
    for w in range(0,len(base)):
        row.extend(base[w])
        w+=1
    #print(row)  #<-                            verificar se 'row' recebeu todas as letras
    r=0
    x=0
    lb =[]
    while x < len(base):
        lin = row[x] 
        posic= base.find(lin)
            #print (row)
        add= base[posic:]
        add+= base[:posic]
        lb.append(add)   
        r+=1
        print(lb[x])    
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
        x+=1
    print("Table mounted !...")
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Insert the text:  ')
    print ('   ')
    txt = str(input('Text:_     '))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    print ('   ')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    print ('   ')
    print('Set "e" for encrypt')
    print('or')
    print('Set "d" for decrypt') 
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    print('chosen mode')
    mod = str(input('_  '))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    print ('   ')
    os.system('cls' if os.name == 'nt' else 'clear')

    key = keyt(txt)
   
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    # =-=-=-=-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    if mod == 'e' or mod == 'encrypt':
        enc(lb, base,txt,key)
    elif mod == 'd' or mod == 'decrypt':
        dec(base,lb,txt,key)
    return
# =-=-=-=-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# =-=-=-=-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#                   ENCRIPTAR
def enc(lb, base,txt,key):

    h=0
    lin=[]
    y=0
    crip =''
    while h < len(txt):
        while y < len(lb):
            if key[h] == lb[y][1]:
                lin.extend(lb[y])
            y+=1
        pos=base.find(txt[h])
        h+=1
    crip += lin[pos]
            
    print('your text encrypted is: ')
    print(crip)
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    return crip
# =-=-=-=-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#               DECRIPTAR
def dec(base,lb,txt,key):
    s=0
    crip=''
    while s < len(txt):
        l=0
        while l < len(lb):
            if key[s] == lb[l][1]:
                row = lb[l]
            l+=1
        pos = base.find(txt[s])
    crip += row[pos]
    print('your text decrypted is: ')
    print(crip)
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    return crip

# =-=-=-=-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


def keyt(txt):
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    print('Insert the keyword')

    #consição para validar apenas uma letra \/   22-01

    keyt = str(input('Key:_    '))
    os.system('cls')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')

    o=0
    key=[]
    while o < len(txt):
        if txt[o] !=' ':
            d=0
            while d < len(keyt):
                key.extend(keyt[d])   #<- key rebece o tamanho do texto
                d+=1
                o+=1
            d=0
            o+=1
        else:
            key.extend('_')
            o+=1
    return key
# =-=-=-=-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

