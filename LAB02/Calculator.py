##Calculator class to compute operations 

class Calculator:
    def compute(self,operation,a,b):
        res = ""
        if operation == "add":
            res = str(self.add(a,b))
        elif operation == "sub":
            res = str(self.sub(a,b))
        elif operation == "mul":
            res = str(self.mult(a,b))
        elif operation == "div":
            try:
                res = str(self.div(a,b))
            except:
                print("DivException occurred")
                res = ""
        else:
            print("Not valid operation!")
            res = ""
        return res
    
    def add(self, a, b):
        return a+b
    def sub(self, a, b ):
        return a-b
    def mult(self, a, b):
        return a*b
    def div(self, a, b):
        if b == 0:
            raise ValueError("Dividen can't be equal to zero ")
        else:
            return a/b

        
    
