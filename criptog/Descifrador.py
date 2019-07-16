import os
from functions.decimals import *
from functions.octals import *
from functions.hexadecimals import *
from functions.binaries import *

def bases():
    #conteúdo a ser trabalhado
    print('Insert the content for convert:')
    crip = int(input("Insert:_   "))

    def opt():
        print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('Chosen base:')
        print('[1] - For converter binary number.')
        print('[2] - For converter decimal number.')
        print('[3] - For converter octal number.')
        print('[4] - For converter hexadecimal number.')
        print('[5] - For return')
        print('  ')
        bs = int(input('Conversion:_   '))
        return bs

    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    opt()
    if bs ==1:
        print(crip.' To decimal is:'.dec(int(crip)))
        print(crip.' To octal is:'.oct(crip))
        print(crip.' To hexa is:'.hec(crip))
    elif bs == 2
        print(crip.' To binary is:'.bin(crip))
        print(crip.' To octal is:'.oct(crip))
        print(crip.' To hexa is:'.hex(crip))
    elif bs == 3
        print(crip.' To binary is:'.bin(crip))
        print(crip.' To decimal is:'.dec(crip))
        print(crip.' To hexa is:'.hec(crip))
    elif bs == 4
        print(crip.' To binary is:'.bin(crip))
        print(crip.' To decimal is:'.dec(crip))
        print(crip.' To octal is:'.oct(crip))
    elif bs == 5
        def main()
        os.system('cls')
    else
        print 'Option is invalid, try again.'
        opt()
    return

main ()

def main():
    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    # Escolher o mode em que o algoritmo ira operar
    input('-=-=-=-=-=- Decipher -=-=-=-=-=-=-=-=-=-')
    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Chose conversion mode:')
    print("[1] - For conversion of binary bases.")
    print('[2] - For césar´s cipher.')
    print('[3] - tographi of phyton.')
    print('[4] - For base64.')
    print('[5] - For Hash MD5.')
    print('[6] - For cipher of substituition.')
    print('[7] - Fot cipher de vigenére.')
    print(' ')
    mode = (int(input('Chosen:_  '))
#-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    if mode== 1
        bases()
    elif mode == 2
        cc()
    elif mode == 3
        crippy()
    elif mode == 4
        Base64()
    elif mode == 5
        hash64()
    elif mode == 6
        cs()
    elif mode == 7
        cv()
    else
        print 'option invalid, try again.'
        mode = int(input('Option:_  '))
    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    os.system('cls')

print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')  


def cesar():
