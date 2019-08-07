from ProblemFeatures import No
from random import randrange
import copy

class Rainhas:
    # variaveis usadas na busca local
    conflitos = []
    liMenor = [1]

    estado_inicial = [] # gerar matriz inicial
    indice = 8
    for l in range(indice):
        linha = []
        for c in range(indice):
            linha.append("'x'")
        estado_inicial.append(linha)


    def teste_objetivo(self, no, tipo):
        if(tipo == "normal"): #Teste para buscas cegas
            matriz = no.estado
            cont = 0
            for l in range(len(matriz)):
                for c in range(len(matriz)):
                    if (matriz[l][c]=="'Q'"):
                        cont+=1
            if(cont == len(matriz)):
                 return True
            return False
        else: #Teste para buscas locais
            cont=0
            for i in range(len(self.liMenor)):
                if(self.liMenor[i]<=1): #Se o custo das posicoes for menor ou igual a 1
                    cont+=1 
            if(cont == len(no.estado)):
                return True
            return False

    def acao(self, no, Busca):
        vetor = []#Vetor de filhos
        if(Busca == "normal"): # Se for busca cega
            matriz = no.estado
            coluna = no.profundidade
            for linha in range(len(matriz)):
                matriz[linha][coluna] = "'Q'"
                Batidas = Rainhas.detectaQs(self, matriz, linha, coluna)
                if(Batidas==0): #Nao ocorreu conflitos
                    aux = copy.deepcopy(matriz)
                    vetor.append(aux) #Vetor de filhos
                matriz[linha][coluna] = "'x'"
            return vetor#Retorna os filhos
        else: #Se for busca local
            Rainhas.conflitos = Rainhas.confli(self,no) #Pega os conflitos
            aux = copy.deepcopy(no.estado)
            Rainhas.liMenor, menor = Rainhas.melhorfilho(self,self.conflitos)#Melhor filho
            select = randrange(0,len(self.liMenor))#Selecionar um dos melhores filhos
            contador = -1
            for i in range(len(self.conflitos)):
                for j in range(len(self.conflitos)):
                    if(menor == self.conflitos[i][j]):#Procurar o melhor filho selecionado
                        contador+=1 #Depende da quantiadade de melhores filhos
                    if(contador==select):#Achou
                        linha = Rainhas.achaQ(self,aux,j)#Pega linha em que a rainha está
                        aux[linha][j] = "'x'" #Faz a troca
                        aux[i][j] = "'Q'"
                        vetor.append(aux)
                        return vetor #Retorna o filho

    def detectaQs(self, auxMatriz, linha, coluna): #Funcao para detectar se tem ataques
        cont = 0
        for l in range(len(auxMatriz)):
            if(auxMatriz[l][coluna] == auxMatriz[linha][coluna]):
                cont+=1
            for c in range(len(auxMatriz)):
                if(linha == l):
                    if(auxMatriz[linha][c] == auxMatriz[linha][coluna]):
                        cont+=1

        #Principal
        #For seguindo
        c=coluna
        for l in range(linha,len(auxMatriz), 1):
            if(c!=len(auxMatriz)):
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
        for l in range(linha, len(auxMatriz), 1):
            if(c!=-1):
                if(auxMatriz[linha][coluna] == auxMatriz[l][c]):
                    cont+=1
                c-=1
        #For seguindo
        c = coluna
        for l in range(linha, -1, -1):
            if(c!=len(auxMatriz)):
                if(auxMatriz[linha][coluna] == auxMatriz[l][c]):
                    cont+=1
                c+=1
        return cont-6

    def achaQ(self, matriz, col): #Funcao para achar a linha da rainha
        for linha in range(len(matriz)):
            if (matriz[linha][col]=="'Q'"):
                return linha
                
    def ColunaX(self, matriz, coluna): #Funcao para deletar uma coluna
        for linha in range(len(matriz)):
            matriz[linha][coluna]= "'x'"
        return matriz

    def confli(self,no): #Achar os conflitos indiretos e diretos
        conflitos = copy.deepcopy(no.estado)
        for col in range(len(conflitos)): #Coluna por linha
            matriz = copy.deepcopy(no.estado)
            matriz = Rainhas.ColunaX(self,matriz, col)#zera a coluna
            for lin in range(len(conflitos)):
                matriz[lin][col] = "'Q'"#Testar Q's
                Batidas = Rainhas.detectaQs(self,matriz,lin, col)#Contando as batidas (direta)
                matriz = Rainhas.ColunaX(self,matriz, col) #Zerar colunas
                aux = copy.deepcopy(matriz) #Matriz auxiliar
                for proxcol in range(len(conflitos)):#Contar as batidas das proximas colunas(indireta)
                    if (proxcol !=col):#Pra ele pular a coluna em que ele está
                        linha = Rainhas.achaQ(self,aux,proxcol) #Achar o Q da linha
                        Batidas = Batidas + Rainhas.detectaQs(self,aux,linha, proxcol)
                        aux = Rainhas.ColunaX(self,aux, proxcol)#Zera a coluna
                conflitos[lin][col] = Batidas#Matriz de batidas
                Batidas=0
        return conflitos

    def melhorfilho(self,matriz):#Colocar os melhores filhos na lista
        menor = 100
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if(menor>matriz[i][j]):
                    menor=matriz[i][j]
        liMenor=[]
        for i in range(len(matriz)):
            for j in  range(len(matriz)):
                if(matriz[i][j]==menor):
                    liMenor.append(matriz[i][j])
        return liMenor, menor

    