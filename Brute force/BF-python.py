#
from itertools import product

# chars to look for
chars = '0123456789'

# password for find
passw = '323'


# only do lengths of
for length in range(1, 4): 

    # recept attempt for pass, by function of itertools.product
    #repete o comprimento do length fazendo a comparação cartesiana dos caracteres
    to_attempt = product(chars, repeat=length)

    #if attempt in to 'to_attempt'
    for turn in to_attempt:
        #turn received string attempt for compare
        turn=''.join(turn)
        print(turn)
        # condition in case turn match pass
        if turn == passw:
            print('pass as found ! '+ turn)
            break;
            
                