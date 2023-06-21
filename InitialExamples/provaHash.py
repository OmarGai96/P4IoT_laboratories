myTable = {"000": "Rossi Paolo", "001": "Dalmasso Ettore", "002":"Dogliani Luca"}
print('first element: ', myTable["000"])

#insert
myTable["003"] = "Martino Fausti"

#delete
del myTable["002"] 

#overwrite
myTable["003"] = "Fodare Umberto"

print('All keys of my table: ')
keys=myTable.keys()
for i in keys:
	print(i)
	
print('All values of my table: ')
val=myTable.values() 
for i in val:
	print(i)
	
print('All items of my table: ')
items=myTable.items()
for i in items:
	print(i)

res="000" in myTable
print('Paolo Rossi è presente? ', res)

