
while True:
    s1 = str(input('enter string one please, type quit to quit: '))
    s2 = str(input('enter string two please, type quit to quit: '))

    if s1 or s2 == 'quit':
        break
    else:
        print('For string one you entered {0} which is '.format(s1), len(s1), 'chars long.')
        print('For String two you entered {0 }which is '.format(s2), len(s2), 'chars long.')
        
    
        