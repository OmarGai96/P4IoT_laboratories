
fw=open('myFile.txt','w')    ##open in write mode
fw.write('Line to write on file')
fw.close()

f=open('myFile.txt')        ##open in read mode (default)
fileContent=f.readline()    ##read the content of the file
print(fileContent)
f.close()

fa=open('myFile.txt','a')    ##open in append mode
fa.write('\nAnother line')
fa.close()

print("\nThis is the final content of your file\n\n")

a = True
f=open('myFile.txt')        ##open in read mode (default)

while a:
    fileContent =f.readline()
    if not fileContent:     
        #EOF reached 
        a = False
    else:
        #not EOF, so print content of file
        print(fileContent)

f.close()
