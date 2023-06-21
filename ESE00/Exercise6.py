lista = [1,2,3,4,5]
rem = lista.pop()
print(f"Removed element {rem}") #removes item 5
rem = lista.pop(2)
print(f"Removed element {rem}") #removes item 3

lista.append(5)
lista.insert(2,3)

print("Regenerated list")

for i in lista:
    print (f"{i} ", end="")