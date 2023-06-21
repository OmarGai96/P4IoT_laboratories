##PROVA DI UNA FUNZIONE

def myfunc(a, b):
    "documentation of function myfunc"
    print(f"Sum of {a} and {b} is {a+b}")
    return

def product(a, b):
    return a * b

if __name__ == "__main__":
    a=10
    b=20
    myfunc(a,b)
    prod=product(a,b)
    print(f"The product is {prod}")

