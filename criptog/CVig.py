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
    if mod == 'e' or mod == 'encrypt':
        print('Insert the text for encrypt')
        print ('   ')
        txt = str(input('Text:_     '))

        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
        print ('   ')
        print('Now insert the key')
        keyt = str(input('Key:_    '))
# =-=-=-=-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        o=0
        while o <= len(txt):
            d=0
            if txt[o] != " ":
                key=[]
                while d < len(keyt):
                    key.extend(keyt[d]) # <- key recebe o tamanho do texto a ser cifrado
                    d+=1
                else:
                    d=0 #<- zera o contador do tamanho da key caso atinja o limite
            else:
                key.extend('_') #<- adiciona caso o txt tiver espaço
            o+=1
# =-=-=-=-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        m=0
        while m <= len(txt): #<- loop para varrer o texto
            e=0
            while e <= len(lb):
                if key[m] == lb[e][0]: #<- loop para encontrar a chave igual a primeira coluna
                    col= lb[e] #<- recebe a linha da chave
                    print(col)
                    cm = txt[m]
                    for cm in base:
                        pos= base.find(cm) #<- recebe a posiçao da letra do texto na base
                    crip = col[pos] #<- recebe a posição da letra na coluna da chave
                    print (crip)


            


# letra da palavra é a linha,  a chave é a colina 1
cv()
