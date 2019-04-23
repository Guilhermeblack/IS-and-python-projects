import math
fim = 4
while fim != '':
    ang = float(input('digite o ângulo que deseja calcular: '))
    sen = math.sin(math.radians(ang))
    print('o angulo de {} tem o seno de {:.2}'.format(ang, sen))
    cos = math.cos(math.radians(ang))
    print('O ângulo de {} tem o cosseno de {:.2}'.format(ang, cos))
    tan = math.tan(math.radians(ang))
    print('O ângulo de {} tem a tangente de {:.2}'.format(ang, tan))
    fim = input(' ')

