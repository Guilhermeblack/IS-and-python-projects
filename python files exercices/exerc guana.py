nlist = int(input(f'quantos elementos terá a lista ?\n'))
list = []
for i in range(nlist):
    elist = int(input(f'qual o valor do número da posição da lista ?\n'))
    list.append(elist)
    i+= 1

print(list) 
i=0 
mv = 0
if mv < range(list):
    mv = list[i]
    i+= 1
print('o maior valor é ', mv)
i=0
mev = 10
if mev > range(list):
    mev = list[i]
    i +=1
print('o menos valor é ', mev)