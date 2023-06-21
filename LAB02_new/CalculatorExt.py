from Calculator import *

class CalculatorExt(Calculator):
    def __init__(self,name):
        super().__init__(name)
        operandList = []
        
    def compute(self, oper, myList):
        self.operandList = myList
        if oper == "add":
            res = 0
        elif oper == "sub":
            res = 2*myList[0]
        elif oper == "mul":
            res = 1
        elif oper == "div":
            res =myList[0]*myList[0]
        else:
            print("Not allowed operation, retry")
            return "wrong operation"
        
        for el in myList:
            res = super().calculate(oper,res,el)
            if res == "null":
                break
        return res
    
    def getOperands(self):
        return self.operandList