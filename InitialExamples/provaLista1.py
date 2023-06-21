array=[99, "bottle of beer", ["on","the","wall"],12,1000]
print('\nContenuto di array:\n')
for i in array:
    print(i)
print('\nConcatenazione:\n')
array2=array+array
for k in array2:
    print(k)
print('\nIntervallo: ',array[1:3])
print('\nUltimo elemento: ',array[-1])
print('\nLunghezza: ',len(array))
print('\nRimpiazzo degli elementi ')
array[1]=23
array[2]=57
for i in array:
    print(i)
print('Elimino ultimo elemento')
del array[-1]
for i in array:
    print(i)



