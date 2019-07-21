def cv():  
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    print('-=-=-=-=-=-=-=-=-=-Vigenére Cypher-=-=-=-=-=-=-=-=-=-')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
    base= 'abcdefghijklmnopqrstuvwxyz'

    row = []
    for w in range(0,len(base)):
        row.extend(base[w])
        w+=1

    r=1
    x=0
    lb =[]
    while x <= len(base): 
        
        for row[x] in base:
            posic= base.find(row[x])
            #print (row)
            if posic<0 or posic > len(base):
                print('error')
            else:
                add = [row[posic:], row[:posic]]
                lb.append(add)
            
            r+=1
            
        print(lb[x])
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')
        x+=1
    print ('   ')    
cv()
