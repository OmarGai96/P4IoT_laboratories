##PROVA FUNZIONE

def func(a,b):
    "Sum of a and b"
    return a+b


lista=list(range(10))
print("This is my list")
for k in lista:
    print(k, end=' ')
print("\nModified list")
for i in lista:
    print(func(i,i+1), end=' ')

    
