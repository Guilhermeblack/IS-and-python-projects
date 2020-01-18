import os

def cryp(Fernet):
    print("modo de cryptografia python, com chave simétrica\n")
    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
    mod = str(input('deseja encriptar ou decriptar os dados ? \n'))
    os.system('cls')
    if mod == 'e' or mod == 'encriptar':
        enc(Fernet)
    elif mod == 'd' or mod == 'decriptar':
        dec(Fernet)
    else:
        input('opção invalida, tente novamente')
        cryp(Fernet)



def enc(Fernet):
    key = Fernet(Fernet.generate_key())
    print(' Key gerada: \n ', key)
    print('entre com a mensagem a ser criptografada:')
    msg = str(input('__   '))
    cripted = key.encrypt(msg)
    os.system('cls')
    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
    print(' sua mensagem: \n', cripted)
    return key, cripted



def dec(Fernet):
    print('insira a mensagem a ser descifrada:')
    msg = str(input('__  '))
    print('-=-=-=---=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
    print('insira a chave assimétrica: ')
    key = str(input('__  '))
    os.system('cls')
    decripted = key.decrypt(msg)
    print('sua mensagem: \n', decripted)
    return msg

