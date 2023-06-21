#ESERCIZIO 1
nomi=('Numa', 'Tullio', 'Anco')
cognomi=('Pompilio', 'Ostilio', 'Marzio')
lista=[]

for i,k in zip(nomi,cognomi):    #accedere a due liste contemporane
    lista.append({'nome':i, 'cognome':k})

for l in lista:
    print(l)

#ESERCIZIO 2
diz={'nome':'Name','cognome':'Surname'}
diz['matricola']= 012345

#ESERCIZIO 3
stringa=input('Immetti valori: ' )
for i in stringa:
    if i == 'A' or i == 'a':
        print('T')
    elif i == 'T' or i == 't':
        print('A')
    elif i == 'G' or i == 'g':
        print('C')
    elif i == 'C' or i == 'c':
        print('G')
    elif i == ',' or i == ' ':
        continue
    else:
        print('Letter not valid')
        break
    
#ESERCIZIO 4
numeri=list(range(500))
sum=0
for i in numeri:
    sum += i

print('La somma è: ', sum)

#ESERCIZIO 5
stringa='abcdefghi'
k=1 #cnt
for i in stringa:
    print('Lettera ',k,': ',i)
    k+=1

#ESERCIZIO 6
print('Immettere una stringa: ')
stringa=input()
while(stringa != 'exit'):
    print(stringa, ' è lunga ', len(stringa))
    stringa=input()



    
           
                  
