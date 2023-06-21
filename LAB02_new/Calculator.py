class Calculator ():
    def __init__(self,name):
        self.name=name

    def calculate(self, operation, oper1, oper2):
        
            if  operation == "add":
                return oper1+oper2
                
            elif operation == "sub":
                return oper1-oper2
                
            elif operation == "mul":
                return oper1*oper2
                
            elif operation == "div":
                try:
                   res = self.div(oper1,oper2)
                   return res
                except:
                    print("DivException occurred")
                    return "null"
                
            else:
                print("Not allowed operation, retry")
                return "wrong operation"
            
    def div(self, a, b):
        if b == 0:
            raise ValueError("Dividen can't be equal to zero ")
        else:
            return a/b       
                