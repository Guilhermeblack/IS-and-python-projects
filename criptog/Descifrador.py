import os
import sys
from cesarcipher import ccipher
from CVig import cv
from cryptog import cryp
from cryptography.fernet import Fernet



def cyp(Fernet):
    cryp(Fernet)
    os.system('cls')



def bases():
    #conteúdo a ser trabalhado
    print('Insert the content for convert:')
    crip = int(input("Insert:_   "))

    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
    print('Chosen base:')
    print('[1] - For converter binary number.')
    print('[2] - For converter decimal number.')
    print('[3] - For converter octal number.')
    print('[4] - For converter hexadecimal number.')
    print('[5] - For return')
    print('  ')
    num = int(input('Conversion:_   '))
    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
    while num <0 and num >5:
        print('Option is invalid, try again.')
        num = int(input('Conversion:_   '))
        os.system('cls')
    os.system('cls')

    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
    if num ==1:
        translate= int(crip,10)
        print(str(crip)+' To decimal is:'+ str(translate))
        translate= oct(crip)
        print(str(crip)+' To octal is:'+str(translate))
        translate= hex(crip)
        print(str(crip)+' To hexa is:'+str(translate))
        print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
        opc = str(input('Want to perform another conversion ?\n'))
        if opc == 'sim' or opc == 's':
            main()
        elif opc == 'nao' or opc == 'n':
            print("Thanks for using my software.\n")
            os.system('cls')
            sys.exit()
    elif num == 2:
        translate = bin(crip)
        print(str(crip)+' To binary is:'+str(translate))
        translate = oct(crip)
        print(str(crip)+' To octal is:'+str(translate))
        translate = hex(crip)
        print(str(crip)+' To hexa is:'+str(translate))
        print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
        opc = input('Want to perform another conversion  ?\n')
        if opc == 'sim' or opc == 's':
            main()
        elif opc == 'nao' or opc == 'n':
            print("Thanks for using my software.\n")
            os.system('cls')
            sys.exit()
    elif num == 3:
        translate = bin(crip)
        print(str(crip)+' To binary is:'+str(translate))
        translate = int(crip,10)
        print(str(crip)+' To decimal is:'+str(translate))
        translate = hex(crip)
        print(str(crip)+' To hexa is:'+str(translate))
        print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
        opc = input('Want to perform another conversion ?')
        if opc == 'sim' or opc == 's':
            main()
        elif opc == 'nao' or opc == 'n':
            print("Thanks for using my software.\n")
            os.system('cls')
            sys.exit()
    elif num == 4:
        translate= bin(crip)
        print(str(crip)+' To binary is:'+str(translate))
        translate = int(crip)
        print(str(crip)+' To decimal is:'+str(translate))
        translate = oct(crip)
        print(str(crip)+' To octal is:'+str(translate))
        print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
        opc = input('Want to perform another conversion ?')
        if opc == 'sim' or opc == 's':
            main()
        elif opc == 'nao' or opc == 'n':
            print("Thanks for using my software.\n")
            os.system('cls')
            sys.exit()
    elif num == 5:
        main()
        os.system('cls')
    else:
        print('Option is invalid, try again.')


    return


def cc(ccipher):
    ccipher()
    os.system('cls')
    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
    print('Want to perform another conversion ?')
    print('Press "s" to yes or "n" to no.')
    opc = input('Option_   ')

    if opc == 'sim' or opc == 's':
        main()
    elif opc == 'nao' or opc == 'n':
        input("Thanks for using my software.\n")
        os.system('cls')
        sys.exit()
    return

def cvig(cv):
    cv()
    os.system('cls')
    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
    print('Want to perform another conversion ?')
    print('Press "s" to yes or "n" to no.')
    opc = input('Option_   ')

    if opc == 'sim' or opc == 's':
        main()
    elif opc == 'nao' or opc == 'n':
        input("Thanks for using my software.\n")
        os.system('cls')
        sys.exit()

def main():
    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

    # Escolher o mode em que o algoritmo ira operar
    print('-=-=-=-=-=- Decipher -=-=-=-=-=-=-=-=-=-\n')
    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
    print('Chose conversion mode:')
    print("[1] - For conversion of binary bases.")
    print('[2] - For césar´s cipher.')
    print('[3] - For cipher vigenere')
    print('[4] - For base64.')
    print('[5] - For Hash MD5.')
    print('[6] - For cipher of substituition.')
    print('[7] - Python cryptography with key.')
    print(' ')
    mode = int(input('Chosen:_  '))
    os.system('cls')
#-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    if mode== 1:
        bases()
        os.system('cls')
    elif mode == 2:
        cc(ccipher)
        os.system('cls')
    elif mode == 3:
        cvig(cv)
        os.system('cls')
    elif mode == 7:
        cyp(Fernet)
        os.system('cls')
    else:
        while mode<1 and mode> 7:
            print ('option invalid, try again.')
            mode = int(input('Option:_  '))
    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
    os.system('cls')

print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')  

main()

