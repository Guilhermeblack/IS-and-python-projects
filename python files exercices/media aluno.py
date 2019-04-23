print('calcuular as notas e media do aluno')
name= input('digite o nome do aluno')
n1 = int(input('difite a primeira nota'))
n2 = int(input('digite a segunda nota'))
n3 = int(input('digite a terceira nota'))
m = (n1+n2+n3) / 3

print('a media do aluno ({}) é{}'.format(name, m))