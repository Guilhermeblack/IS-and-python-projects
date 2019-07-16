import os
import sys

def ccipher():
    print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("-=-=-=--=-=-=-=-Cesar´s Cipher-=-=-=-=-=-=-=-=-\n")
    print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print(" ")

    #recebe a key de critografia e valida
    key = int(input("Enter the key for this cryptography  (ate 26)\n"))
    while key > 26 or key < 0:  
        print(" ")
        key = input("This key is invalid, try again.")

    base = 'abcdefghijklmnopqrstuvwxyz'
    os.system('cls')

    #escolhe o modo
    print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Do you want to encrypt-> enter (e)")
    print(" or ")
    print('decrypt-> enter (d) ?\n')
    modo = input('Option_   ')
    os.system('cls')

    #insere e formata o texto
    print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("Insert the message to be converted:\n")
    text= input('Message_    ')
    print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    text = text.lower()
    os.system('cls')

    #insere o texto final
    cripto =''

        #escolhe o modo
    if (modo == 'e' or modo == 'encriptar'):
        for word in text:
                    #encontra o numero da posição dp word na base
            posicion = base.find(word)
            if posicion != " ":
                #soma a key á posição
                posicion += key
                # se a posição for maior que a base ira calcular a diferença
                if(posicion > len(base)):
                    posicion = posicion - len(base)
            else:
                cripto= cripto +"_"
        #concatena a o word encontrado           
            cripto = cripto + base[posicion]

    elif (modo == 'd' or modo == 'decriptar'):
            # contador do texto
                # recebe o word da posição
                #condição se o word estiver contido na base
        for word in text:
                #encontra a posição
            posicion = base.find(word)
                #subtrai a key
            if posicion != " ":
                posicion -= key
                #condicional se a posição foi menor que 0
                if posicion < 0:
                    # subtrai o valor absoluto da base para encontrar a posição
                    posicion = len(base)- abs(posicion)
            else:
                cripto = cripto + "  _  "
        #resultado            
            cripto = cripto +base[posicion]
    print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print("Your message is:  \n" + cripto)
    print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    s= input(" ")
    return