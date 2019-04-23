print ('Analisador de Nome\n')

#essa parte analisa quantas letras tem no texto sem espaços

text = input('digite o texto a ser analisado:\n')
tamtext = len(text)
i=0
numlet=0
for i in range(tamtext):
    if text[i] != ' ':
        i += 1
        numlet += 1 
print("a quantidade de letras é de:", numlet, 'letras no texto')

# dividir o texto em uma lista e contar as palavras

listtext = text.split()
qntword = len(text.split())
print ('---\n')
print('a quantidade de palavras é de :', qntword, 'palavras\n')

primword = int(input('qual a quantidade de vezes a palavra deve aparecer para ser destaque ?\n'))

# contar quantas vezes um item aparece no texto

import collections
vzsword= collections.Counter(listtext).most_common(primword)
print(vzsword,'\n')
i=0
numvzs = len(vzsword)
print(numvzs) #aq
while i in range(vzsword):
    # algum erro na linha abaixo
    numtext = listtext[i]
    txtn = listtext.count(numtext)
    print('A palavra', listtext[i], 'aparece', txtn,'vezes no texto\n')
    if txtn >= primword:
        worddest= [listtext[i]]
        print('a palavra', listtext[i],'se destaca\n')
    i+=1


#gui manda no mkt gui mkt xambra gui manda gui mkt
# contar se uma palavra aparece certas vezes e se aparecer, qual o total de vezes
