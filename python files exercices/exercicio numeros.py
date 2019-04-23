print('exercicios yt\n')
print('=-'* 12)
list = []
d = 's'
while d == 's':
    n = int(input('digite um número:\n'))
    list.append(n)
    d = input('deseja continuar? (s/n) ?')
    print('=-'* 12)

for i, v in enumerate(list):

    print('a {}ª posição equivale ao {} número.\n'.format(i+1,v))

print('=-'* 12)
nl = int(input('qual numero deseja saber se esta na lista?\n'))
l=int(0)
s= int(len(list))
ga = 0
while l < s:
    if nl == list[l]:
        ga +=1
    l+=1
print('=-'* 12)
print('o numero {} aparece {} vezes na contagem'.format(nl, ga))
print('seu resultado esta em construção...')
