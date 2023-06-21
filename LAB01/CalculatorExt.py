#Extension of class Calculator
from Calculator import * 

class CalculatorExt(Calculator):
    def computeExt(self,operation,lista):
        finalRes=""
        first = 1
        res=0

        for i in lista:
            if operation == "add":
                res = Calculator.add(self,res,i)
            elif operation == "sub":
                if first == 1:
                    first = 0
                    res = Calculator.add(self,res,i)  ##first operand must be ADDED 
                else:
                    res = Calculator.sub(self,res,i)
            elif operation == "mul":
                if first==1:
                    first = 0
                    res = Calculator.mult(self,1,i)  ##first operand must be ADDED 
                else:
                    res = Calculator.mult(self,res,i)
            elif operation == "div":
                if first==1:
                    first = 0
                    res = Calculator.mult(self,1,i)  ##first operand must be ADDED 
                else:
                    try:
                        res = Calculator.div(self,res,i)
                    except:
                        print("DivException occurred")
                        res = ""
            else:
                print("Not valid operation!")
                res = ""
        finalRes = str(res)
        return finalRes

        
    
