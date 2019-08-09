import copy
from random import randrange


def SelectMask():
    a = randrange(0,1)
    if(a==0):
        return [0,0,0,0,1,1,1,1]
    else:
        [1,1,0,0,0,0,1,1]
lista =[]

a = [1,3,4,5,6,7,0,2]
b = [4,5,3,2,1,7,6,0]

lista.append(a)
lista.append(b)
while(True):
    if(len(lista)>=16):
        break
    a = randrange(0,len(lista))
    b = randrange(0,len(lista))
    while(b==a):
        b = randrange(0,len(lista))
    lista1 = []
    lista2 = []
    mask = SelectMask()
    for i in range(len(mask)):
        if(mask[i]==0):
            lista1.append(lista[a][i])
            lista2.append(lista[b][i])
        if(mask[i]==1):
            lista1.append(lista[b][i])
            lista2.append(lista[a][i])
    lista.append(lista1)
    lista.append(lista2)
print(lista)

