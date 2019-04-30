print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Criptografia de César")
print(" ")

#recebe a chave de critografia e valida
chave = int(input("digite a chave de criptografia (ate 26)\n"))
while chave > 26 or chave < 0:  
    print(" ")
    chave = input("chave inválida, tente novamente")

base = 'abcdefghijklmnopqrstuvwxyz'

#escolhe o modo
modo = str(input("Deseja encriptar ou descriptar\n"))

#insere e formata o texto
text= input("Digite o texto a ser criptografado\n")
tamanho_txt = len(text)
text = text.lower()

#posicion = 0
#insere o texto final
cripto =''

#def crip(chave, base, modo, texto, txt,cripto):
char = 0
    #escolhe o modo
if (modo == 'e' or modo == 'encriptar') :
    
    while char <= tamanho_txt:

            #recebe o caractere de comparação
        caractere = text[char]

            #enquanto o caractere estiver coontido na base de comparação
        for caractere in base[0:len(base)]:

                #encontra o numero da posição dp caractere na base
            posicion = base.find(caractere)

                #soma a chave á posição
            posicion + chave

                # se a posição for maior que a base ira calcular a diferença
            if(posicion > len(base)):
                posicion = posicion - len(base)

        #concatena a o caractere encontrado           
        cripto = cripto + base[posicion]

        char = char +1
                    
if (modo == 'd' or modo == 'decriptar'):
        # contador do texto
    while char <= tamanho_txt:
            # recebe o caractere da posição
        caractere = text[char]
            #condição se o caractere estiver contido na base
        for caractere in base[0:len(base)]:
                #encontra a posição
            posicion = base.find(caractere)
                #subtrai a chave
            posicion - chave
                #condicional se a posição foi menor que 0
            if posicion <= 0:
                    # subtrai o valor absoluto da base para encontrar a posição
                posicion = len(base)- abs(posicion)
                    
        #resultado            
        cripto = cripto + base[posicion]
        char = char + 1      

     #   return cripto
print("sua mensagem \n" + cripto)