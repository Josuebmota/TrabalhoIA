from ProblemFeatures import No, Auxiliar
from random import randrange
import copy

class Rainhas:
    # variaveis usadas na busca local

    estado_inicial = [] # gerar matriz inicial
    indice = 8
    for l in range(indice):
        linha = []
        for c in range(indice):
            linha.append("'x'")
        estado_inicial.append(linha)


    def teste_objetivo(self, no, tipo):
        if(tipo == "cega"): #Teste para buscas cegas
            matriz = no.estado
            cont = 0
            for l in range(len(matriz)):
                for c in range(len(matriz)):
                    if (matriz[l][c]=="'Q'"):
                        cont+=1
            if(cont == len(matriz)):
                 return True
            return False

    def acao(self, no, Busca):
        vetor = []#Vetor de filhos
        if(Busca == "cega"): # Se for busca cega
            matriz = no.estado
            coluna = no.profundidade
            for linha in range(len(matriz)):
                matriz[linha][coluna] = "'Q'"
                Batidas = Auxiliar.detectaQs(self, matriz, linha, coluna)
                if(Batidas==0): #Nao ocorreu conflitos
                    aux = copy.deepcopy(matriz)
                    vetor.append(aux) #Vetor de filhos
                matriz[linha][coluna] = "'x'"
            return vetor#Retorna os filhos