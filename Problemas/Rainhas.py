from ProblemFeatures import No
import copy

class Rainhas:

    
    estado_inicial = []
    indice = 8
    for l in range(indice):
        linha = []
        for c in range(indice):
            linha.append("'x'")
        estado_inicial.append(linha)


    def teste_objetivo(self, no):
        matriz = no.estado
        cont = 0
        for l in range(len(matriz)):
            for c in range(len(matriz)):
                if (matriz[l][c]=="'Q'"):
                    cont+=1
        if(cont == len(matriz)):
            return True
        return False
    
    def acao(self, no):
        matriz = no.estado
        coluna = no.profundidade
        vetor = []
        for linha in range(len(matriz)):
            matriz[linha][coluna] = "'Q'"
            #Linha e coluna
            cont = 0
            for l in range(len(matriz)):
                if(matriz[l][coluna] == matriz[linha][coluna]):
                    cont+=1
                for c in range(len(matriz)):
                    if(linha == l):
                        if(matriz[linha][c] == matriz[linha][coluna]):
                            cont+=1

            #Principal
            #For seguindo
            c=coluna
            for l in range(linha,len(matriz), 1):
                if(c!=len(matriz)):
                    if(matriz[linha][coluna] == matriz[l][c]):
                        cont+=1
                    c+=1
            #For voltando
            c = coluna
            for l in range(linha, -1, -1):
                if(c!=-1):
                    if(matriz[linha][coluna] == matriz[l][c]):
                        cont+=1
                    c-=1
            #Secundaria
            #For voltando
            c= coluna
            for l in range(linha, len(matriz), 1):
                if(c!=-1):
                    if(matriz[linha][coluna] == matriz[l][c]):
                        cont+=1
                    c-=1
            #For seguindo
            c = coluna
            for l in range(linha, -1, -1):
                if(c!=len(matriz)):
                    if(matriz[linha][coluna] == matriz[l][c]):
                        cont+=1
                    c+=1

            if(cont==6):
                aux = copy.deepcopy(matriz)
                vetor.append(aux)

            matriz[linha][coluna] = "'x'"
        return vetor