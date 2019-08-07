import copy
from random import randrange
# matriz = [["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"],
#           ["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"],
#           ["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"],
#           ["'x'","'x'","'x'","'Q'","'x'","'x'","'x'","'x'"],
#           ["'Q'","'x'","'x'","'x'","'Q'","'x'","'x'","'x'"],
#           ["'x'","'Q'","'x'","'x'","'x'","'Q'","'x'","'Q'"],
#           ["'x'","'x'","'Q'","'x'","'x'","'x'","'Q'","'x'"],
#           ["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"]]

def gerarMatriz():
    matriz = []
    indice = 8
    for l in range(indice):
        linha = []
        for c in range(indice):
            linha.append("'x'")
        matriz.append(linha)
    for c in range(indice):
        n= randrange(0,7)
        matriz[n][c] = "'Q'"
    return matriz
        

def ColunaX(matriz, coluna):
    for linha in range(len(matriz)):
        matriz[linha][coluna]= "'x'"
    return matriz

def detectaQs(auxMatriz, linha, coluna):
    cont = 0
    for l in range(len(matriz)):
        if(auxMatriz[l][coluna] == auxMatriz[linha][coluna]):
            cont+=1
        for c in range(len(matriz)):
            if(linha == l):
                if(auxMatriz[linha][c] == auxMatriz[linha][coluna]):
                    cont+=1

    #Principal
    #For seguindo
    c=coluna
    for l in range(linha,len(matriz), 1):
        if(c!=len(matriz)):
            if(auxMatriz[linha][coluna] == auxMatriz[l][c]):
                cont+=1
            c+=1
    #For voltando
    c = coluna
    for l in range(linha, -1, -1):
        if(c!=-1):
            if(auxMatriz[linha][coluna] == auxMatriz[l][c]):
                cont+=1
            c-=1
    #Secundaria
    #For voltando
    c= coluna
    for l in range(linha, len(matriz), 1):
        if(c!=-1):
            if(auxMatriz[linha][coluna] == auxMatriz[l][c]):
                cont+=1
            c-=1
    #For seguindo
    c = coluna
    for l in range(linha, -1, -1):
        if(c!=len(matriz)):
            if(auxMatriz[linha][coluna] == auxMatriz[l][c]):
                cont+=1
            c+=1
    return cont-6

def achaQ(matriz, col):
    for linha in range(len(matriz)):
        if (matriz[linha][col]=="'Q'"):
            return linha


matriz = gerarMatriz()
conflitos = []
for l in range(len(matriz)):
    linha = []
    for c in range(len(matriz)):
        linha.append(1)
    conflitos.append(linha)
cont = 0
for col in range(len(matriz)):
    auxMatriz = copy.deepcopy(matriz)
    auxMatriz = ColunaX(auxMatriz, col)
    for lin in range(len(matriz)):
        auxMatriz[lin][col] = "'Q'"
        cont = detectaQs(auxMatriz,lin, col)
        auxMatriz = ColunaX(auxMatriz, col)
        aux2Matriz = copy.deepcopy(auxMatriz)
        for proxcol in range(len(matriz)):
            if (proxcol !=col):
                linha = achaQ(aux2Matriz,proxcol)
                cont = cont + detectaQs(aux2Matriz,linha, proxcol)
                aux2Matriz = ColunaX(aux2Matriz, proxcol)
        conflitos[lin][col] = cont
        cont=0
menor = conflitos[0][0]
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if(menor>conflitos[i][j]):
            menor=conflitos[i][j]
liMenor=[]
for i in range(len(conflitos)):
    for j in  range(len(conflitos)):
        if(conflitos[l][j]==menor):
            liMenor.append(conflitos[l][j])
select = randrange(0,len(liMenor))
contador = -1
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if(menor == conflitos[i][j]):
            contador+=1
        if(contador==select):
            linha = achaQ(matriz,j)
            matriz[linha][j] = "'x'"
            matriz[i][j] = "'Q'"

for i in range(len(matriz)):
    for j in range(len(matriz)): 
        print(conflitos[i][j]," ", end="")
    print()
print("\n")

for i in range(len(matriz)):
    for j in range(len(matriz)): 
        print(matriz[i][j]," ", end="")
    print()
print("\n")