print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Criptografia de César")
print(" ")

chave = int(input("digite a chave de criptografia (ate 26)\n"))
while chave > 26 or chave < 0:  
    print(" ")
    chave = input('chave inválida, tente novamente')

base = 'abcdefghijklmnopqrstuvwxyz'

modo = str(input("Deseja encriptar ou descriptar\n"))

text= input("Digite o texto a ser criptografado\n")
texto = text(range(len(text)))
#texto = texto.lower()
#texto.split()
txt = int(len(texto))
num = 0
cripto = ''

#'''def crip(chave, base, modo, texto, txt):'''
if (modo == 'e' or modo == 'encriptar') :

    while txt>= 0:
        for texto[txt] in base(range(len(base))):
            num = base.find(texto[txt])
            num= num + chave
            if(num > len(base)):
                    num = num- len(base)
                    cripto = cripto + base[num]
    txt= txt -1
                    
if (modo == 'd' or modo == 'decriptar'):
    while txt>= 0:
        for texto[txt] in base[0:len(base)] :
            num = base.find(texto[txt])
            num = num - chave
            if num < 0:
                num = len(base)- abs(num)
                cripto = cripto + base[num]
    txt = txt -1      
#    '''return cripto'''
print("sua mensagem \n" + cripto)