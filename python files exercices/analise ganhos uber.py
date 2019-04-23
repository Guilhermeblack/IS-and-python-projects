g = 8
while g != ''
print('Calculador de ganhos \n')
opr= 5
while opr != 0:
    print('Escolha a seguir o que deseja fazer:\n')
    print('Digite "1" para calcular seus ganhos:')
    print('digite "2" para calcular o rendimento do seu veículo:')
    print('Digite "0" para finalizar e salvar os resultados')
    opr = int(input('Qual sua opção ?'))
    if opr == 1:
        opc = 's'
        while opc != 'n':
            lucro = float(input('quanto foi seu ganho bruto no dia ?\n'))
            vlrcomb = float(input('quanto foi gasto com combustível ?\n'))
            vlrpes = float(input('quanto foi o gasto pessoal ?\n'))
            ganho = float(vlrcomb + vlrpes)
            ganbrut = float(lucro - ganho)
            print('Seu ganho foi de R$:', ganbrut,'reais.\n')
            listresult.insert(0, ganbrut)
            print(listresult)
            opc = input('Deseja realizar outra operação de ganhos? (s/n)')
            opr = input('Se desejar sair digite "0"')
            c = input('pressione enter para avançar.')

    if opr == 2:
        while opc == 's':
            qnthrs = float(input ('quantas horas por dia ficou online ?\n'))
            medh = float(ganbrut /qnthrs)
            precomb = float(input ('quanto pagou no combustível por litro ?\n'))
            kmini = float(input('qual quilometragem inicial ?\n'))
            kmfin = float(input('qual quilometragem final ?\n'))
            kmrod = float(kmfin- kmini)
            qntrend = float(input('quantos quilômetros por litro seu carro faz ?\n'))
            rendmed = kmrod* qntrend
            qntcomb = float(input('Quantos litros de combustível foram gastos nas suas {} horas online? \n'.format(qnthrs)))
            print('Sua média foi de {:.2} reais por hora\n'.format(medh))
            lts = float(vlrcomb/precomb)
            print('Você colocou {:.3} Litros de combustível ao todo\n'.format(lts))
            rendc = float(qntcomb/kmrod)
            rendh = float(qntcomb/qnthrs)
            print('Seu carro rendeu {:.3} litros por quilômetro\n'.format(rendc))
            print('Você fez uma meida de {:.3} litros por hora de combustível\n'.format(rendh))
            print('seu carro gastou em media {:.3} litros'.format(rendmed) )
            print('')
            opc = input(' Deseja realizar outra operação ?')
            opr = input('Se desejar sair digite "0"')

print( 'Obrigado por utilizar o programa ')
g = input('fim')

