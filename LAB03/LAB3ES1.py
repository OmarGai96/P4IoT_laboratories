import json
import requests

if __name__ == '__main__':
    print("LAB 3 Exercise 1\n\n")
    print("We want to use a calculator")
    flag=1
    while(flag):
        print("Available operations: add, sub, mul, div  (type 'exit' to finish)")
        oper=input('Insert operation: ')
        if(oper == 'add' or oper == 'sub' or oper == 'mul' or oper == 'div'):
            op1=input('Insert operand1: ')
            op2=input('Insert operand2: ')
            payload = {'op1': op1, 'op2': op2}
            
            if oper == 'div' and op2 == '0':
                print("For division: divisor error, cannot be 0")
            else:
                req = requests.get("http://localhost:8080/"+oper, params=payload)

                print("Your request is: " +req.url) #useful for debug
                y=json.dumps(req.json())  #y is a string
                myDict = json.loads(y) 
                print("\toperation:      "+myDict['operation'])
                print("\tfirst operand:  "+str(myDict['op1']))
                print("\tsecond operand: "+str(myDict['op2']))
                print("\tresult:         "+str(myDict['result']))
        elif oper=='exit':
            print("Finish")
            flag = 0
        else:
            print("Operation not valid")
            flag = 0
    

