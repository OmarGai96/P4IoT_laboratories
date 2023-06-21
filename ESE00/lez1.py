if __name__=="__main__":
    #This is the main
    print ("Sentence to print")
    print ("Another sentence")  #no \n is needed
    
    value = 4.356434
    print("The average value is: %.2f" %value)  ##to print only 2 decimal numbers
    pi=3.15169265
    print(f"{pi:.4}")

##ESERCIZIO 2
    print("\nEsercizio 2\n")
    name="myName"
    age= 25
    birthday= "1/01/1990"

    print('My name is ', name, ' and I\'m ', age, ' years old, I was born the ', birthday)

##ESERCIZIO 3
    print("\nEsercizio 3\n")

    print("\n\nCompute an addition")
    sum = 2+3
    print(f"2+3={sum}")

##ESERCIZIO 4
    print("\nEsercizio 4\n")

    name=input("What's your name? ")
    print(f"Hello {name}, how are you?")

##ESERCIZIO File

fw=open('myFile.txt','w')    ##open in write mode
fw.write('Line to write')
fw.close()

f=open('myFile.txt')        ##open in read mode
fileContent=f.readline()        ##read the content of the file
f.close()
print(fileContent)

fa=open('myFile.txt','a')    ##open in append mode
fa.write('\nAnother line')
fa.close()

##ESERCIZIO 5

print("\nEsercizio 5\n")
##f1=open("original.txt")
##f2=open("copy.txt",'w')
##f2.write('The content of the original file is:\n')
##line=f1.readline()
##print(line)
##f2.write(line)
##line=f1.readline()
##print(line)
##f2.write(line)
##
##f1.close()
##f2.close()


##ESERCIZIO 5 with while


f1=open("original.txt")
f2=open("copy.txt",'w')
f2.write('The content of the original file is:\n')
print('The content of the original file is:\n')
a=True #is flag

while a:
    line=f1.readline()
    if not line:
        print("\t\t\tEnd of File")
        a = False
    else:
        print(line)
        f2.write(line)
        
f1.close()
f2.close()



##ESERCIZIO LISTA
print('\nEsercizio lista')
numbers=[1,2,3,4,5] ##list
list_len=len(numbers)
sum_of_num=0                          ##EQUIVALENT
for i in range(list_len):             ##for i in numbers:
    sum_of_num += numbers[i]          ##  sum_of_num+=i

print(f"The sum of all values is {sum_of_num}")
prod=1
i=0
while i<list_len:
    prod=prod*numbers[i]
    i+=1
print(f"The product of all values is {prod}")

##ESERCIZIO 6
print("\nEsercizio 6\n")
numero=int(input("Scrivi un numero: "))
if numero%2 == 0:
    print("Number is a multiple of 2")
elif numero%3 == 0:
    print("Number is a multiple of 3")
else:
    print("Not a multiple of 2 or 3")

##ESERCIZIO 7
print("\nEsercizio 7\n")
numbers=[1,2,3,4,5,6,7,8,9,10]
avg=0
maxN=0
minN=99999
summ=0
for i in numbers:
    summ+=i
    if i < minN :
        minN = i
    elif i > maxN:
        maxN = i
    
print(f"Min is {minN}")
print(f"Max is {maxN}")
avg=summ/(len(numbers))
print(f"Average is {avg}")