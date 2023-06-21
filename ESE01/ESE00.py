import json

#Exercise 1

if __name__=="__main__":
    #This is the main
    print ("Sentence to print")
    print("Another sentence")  ##no \n is needed
    
value = 4.356434
print("The average value is: %.2f" %value)  ##to print only 2 decimal numbers
pi=3.15169265
print(f"{pi:.5}") ##to print 5 decimal numbers

#Exercise 2

name="Paolo"
age= 2022-1993
birthday= "11/02/1993"

print('My name is ', name, ' and I\'m ', age, ' years old, I was born the ', birthday)

#Exercise 3

print("\n\nCompute an addition")
print(f"2+3={2+3}")

#Exercise 4

name=input("What's your name? ")        ##able to read also a space character
print(f"Hello {name}, how are you?")

#Exercise File

fw=open('myFile.txt','w')    ##open in write mode
fw.write('Line to write on file')
fw.close()

f=open('myFile.txt')        ##open in read mode (default)
fileContent=f.readline()    ##read the content of the file
f.close()
print("\n\n\nThis is the content of your file\n")
print("-----------------------")
print(fileContent)
print("-----------------------\n\n")

fa=open('myFile.txt','a')    ##open in append mode
fa.write('\nAnother line')
fa.close()

f=open('myFile.txt')        ##open in read mode (default)
print("\n\n\nThis is the final content of your file\n")
print("-----------------------")
fileContent=f.readline()
print(fileContent)
fileContent=f.readline()
print(fileContent)
print("-----------------------\n\n")

##alternatively
a = True
f=open('myFile.txt')        ##open in read mode (default)
print("\n\n\nThis is the final content of your file\n")
print("-----------------------")
while a:
    fileContent =f.readline()
    if not fileContent:
        f.close()
        a = False
    else:
        print(fileContent)
print("-----------------------\n\n")
#Exercise 5

print("\nEsercizio 5\n")
f1=open("original.txt")
f2=open("copy.txt",'w')
f2.write('The content of the original file is:\n')
line=f1.readline()
print(line)
f2.write(line)
line=f1.readline()
print(line)
f2.write(line)

f1.close()
f2.close()


#Exercise 5 with while


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



#Exercise LIST

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

#Exercise 6

numero=int(input("Scrivi un numero: "))
if numero%2 == 0:
    print("Number is a multiple of 2")
elif numero%3 == 0:
    print("Number is a multiple of 3")
else:
    print("Not a multiple of 2 or 3")

#Exercise 7

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

#Exercise 8

##Set all the keys and the empty values and then fill the dictionary
personal_data={
    "projectName": "",
    "company": "",
    "deviceList": [
           {
                "deviceID": "",
                "deviceName": "",
                "deviceType": "",
               
           }
        ]
    }

personal_data['projectName']=input("Write the name of your project: ")
personal_data['company']=input("Write the name of your company: ")
personal_data['deviceList'][0]['deviceID']=input("\tWrite the ID of your device: ")
personal_data['deviceList'][0]['deviceName']=input("\tWrite the name of your device: ")
personal_data['deviceList'][0]['deviceType']=input("\tWrite the type of your device: ")

##additional feature
f=open("dict_content.txt", 'w')
##f.write(f"Project name: {personal_data['projectName']}\n")
##f.write(f"Company:      {personal_data['company']}\n")
##f.write(f"\tDevice ID:    {personal_data['deviceList'][0]['deviceID']}\n")
##f.write(f"\tDevice Name:  {personal_data['deviceList'][0]['deviceName']}\n")
##f.write(f"\tDevice type:  {personal_data['deviceList'][0]['deviceType']}")
json.dump(personal_data,f)
f.close()


