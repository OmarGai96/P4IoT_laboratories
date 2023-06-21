#numeri=[1,2,3,4,5,6,7]
numeri=range(7)
for i in numeri:
    print('Il numero ', i, end=' ')
    if i%2 == 0:
        print(' è pari')
    else:
        print(' è dispari')
