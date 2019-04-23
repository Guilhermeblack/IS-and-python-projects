

print('{:-^60}'.format(' GBlack Store '))

preco = (input('preço da compra: R$'))
print('{:-^60}'.format('formas de pagamento'))
print('''[ 1 ] à vista no dinheiro ou depósito (sujeito à aprovação))
 [ 2 ] à vista no cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão''')

opc = int(input('qual é a opção? '))


if opc == 1:

    total = ( preco - (preco *0,1))
elif opc == 2:
    total = (preco)
elif opc == 3:
    total = (preco * 1,1)
elif opc == 4:
    print('''3 ou 4 parcelas = 20% 
        5 a 8 = 25%
        9 ou mais vezes = 30%''')
    parc = int(input('{:-^60}'.format('quantas parcelas ?')))

if parc == 3 or 4:
        total = (preco * 1,2)
elif parc >= 5 and parc <=8:
        total = (preco * 1,25)
elif parc >8:
        total = (preco * 1,3)
    

print('o total da sua compra vai ser de' + total)