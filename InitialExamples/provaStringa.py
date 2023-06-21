#prova stringa
s='Python'
print(s[0:2])   #Py
print(s[:2])    #Py
print(s[3:5])    #ho
print(s[3:])    #hon
print(s[-2:])    #on

print('\'y\' è presente nella stringa Python: ', 'y' in s)
print('\'x\' è presente nella stringa Python: ', 'x' in s)
print('\'Py\' è presente nella stringa Python: ', 'Py' in s)
print('\'py\' è presente nella stringa Python: ', 'py' in s)
print('\'h\' NON è presente nella stringa Python: ', 'h' not in s)

frutto='Ba'
print(frutto+('na'*2))   # print Banana

parola='Precipitosamente'
print('La parola\"', parola, '\" è lunga', len(parola), 'lettere\n')
maiusc=parola.upper()
print('Tutto maiuscolo: ',maiusc)
minusc=parola.lower()
print('Tutto minuscolo: ',minusc)
print(parola)

##UPPER E LOWER NON SONO UTILIZZABILI PER ALTRI TIPI##


#FORMATTAZIONE
#permette di inserire valori variabili dentro una stringa

print("Immetti una dimensione del raggio: ")
raggio=int(input())
area= 3.14 * raggio**2
circonf=2*3.14*raggio
s="L'area è {}, la circonferenza è {}."
print(s.format(area,circonf))
#oppure

print(f'L\'area è {area}, la circonferenza è {circonf}.')

