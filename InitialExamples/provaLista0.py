stringa=input('Immetti una parola: ')
print('\nConcatenazione: ',stringa+stringa)
print('\nRipetizione: ',stringa*3)
print('\nCarattere: ',stringa[2])
print('\nUltima lettera: ',stringa[-1])
print('\nLunghezza: ',len(stringa))
print('\nRicerca della lettera a: ', "a" in stringa)
if(("a" in stringa) == True): 
    print('\nMolto bene, la lettera \'a\' è presente!')
