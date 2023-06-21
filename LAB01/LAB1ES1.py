###MAIN CLASS
from  Calculator import *

def printJSON(f,operation,a,b,c):
    f.write(f'\n\t"operation": "{operation}",')
    f.write(f'\n\t"operand_1": {a},')
    f.write(f'\n\t"operand_2": {b},')
    f.write(f'\n\t"result"   : {c} ')
    return

if __name__=="__main__":


    ##EXERCISE N 1
    print("EXERCISE 1")
    
    calc=Calculator()
    flag = 1
    print("We want to use a calculator")
    print("Available operations: add, sub, mul, div  (type 'exit' to finish)") 
    f=open("result.json", "w")
    f.write("{")
    i=0
    while(flag):
        oper=input('Insert operation: ')
        if oper == "exit":
            print('Finish')
            flag = 0
        else:
            op1=int(input('Insert operand1: '))
            op2=int(input('Insert operand2: '))
            result = calc.compute(oper,op1,op2)
            if result == "":
                print('Finish')
                flag = 0
            elif i==0:
                f.write(f'\n"operation{i}":')
                f.write(" {")
                printJSON(f,oper,op1,op2,result)
                f.write("\n}")
            else:
                f.write(f',\n"operation{i}":')
                f.write(" {")
                printJSON(f,oper,op1,op2,result)
                f.write("\n}")
        i+=1
    f.write("\n}") ##JSON file closed
    f.close()

    
