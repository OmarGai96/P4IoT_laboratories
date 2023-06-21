if __name__=="__main__":
    fr=open("original.txt")
    fw=open("copy.txt", 'w')
    
    original=fr.read()
    print(original)
    fw.write("The content of the original file is:\n")
    fw.write(original)
    
    fr.close()
    fw.close()
    
    print("\n\n")
    
    f1=open("original.txt")
    f2=open("copy2.txt",'w')
    stringToPrint = "The content of the original file is:\n"
    f2.write(stringToPrint)
    print(stringToPrint,end="")
    a=True #is flag

    while a:
        line=f1.readline()
        if not line:
            print("\n\t\t\tEnd of File reached")
            a = False
        else:
            print(line,end="")
            f2.write(line)
        
    f1.close()
    f2.close()