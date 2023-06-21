a=[0,1,2,3,4]
print('My list')
a
for i in a: 
    print(i)
a.append(5)
a.insert(0,'-1')
rem=a.pop(0)
print('\nHo rimosso: ',rem)
print('\nInverto')
a.reverse()
for i in a:
    print(i)
print('\nOrdino')
a.sort()
for k in a:
    print(k)


