import os
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
    input('_ ')
    os.system('cls')
    print ('   ')
    print('Set "e" for encrypt')
    print('or')
    print('Set "d" for decrypt') 
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    print('chosen mode')
    mod = str(input('_  '))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    print ('   ')
    os.system('cls')

    key()
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')

    if mod == 'e' or mod == 'encrypt':
        enc(key, lb, base)
    elif mod == 'd' or mod == 'decrypt':
        dec(key,lb,base)
# =-=-=-=-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def key(txt,keyt)
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    print ('   ')
    print('Now insert the key')
    keyt = str(input('Key:_    '))
    os.system('cls')
    o=0
    key=[]
    while o <= len(txt):
        if txt[o] != ' ':
            d=0
            while d < len(keyt):
                key.extend(keyt[d])   #<- key rebece o tamanho do texto
                d+=1
                o+=1
            else:
                d=0
                o+=1
        else:
            key.extend('_')
            o+=1
    return key
# =-=-=-=-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#                   ENCRIPTAR
def enc(key,lb,base)
    print('Insert the text for decrypt')
    print ('   ')
    txt = str(input('Text:_     '))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    h=0
    y=0
    crip =''
    while h < len(txt):
        while y < len(lb):
            if key[h] == lb[y][1]:
                row = lb[y]
            y+=1
        pos=base.find(txt[h])
        h+=1
    crip += row[pos]
            
    print('your text encrypted is: ')
    print(crip)
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    input(':_   ')
    return crip
# =-=-=-=-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#               DECRIPTAR
def dec(key,lb,base)
    if mod == 'd' or mod == 'decrypt':
        print('Insert the text for decrypt')
        print ('   ')
        txt = str(input('Text:_     '))
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
        print ('   ')
        print('Now insert the key')
        keyt = str(input('Key:_    '))
        os.system('cls')
    # =-=-=-=-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    s=0
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
    input(':_   ')
# letra da palavra é a linha,  a chave é a colina 1
cv()
