import copy
class Problema: #Caracteristicas do problema que será executado
    def _init_(self, estado_inicial, acoes, teste_objetivo, custo_do_passo):
        self.estado_inicial = estado_inicial
        self.acoes = acoes
        self.teste_objetivo = teste_objetivo
        self.custo_do_passo = custo_do_passo

class No: #Caracteristicas da Posicao
    def _init_(self, estado, pai, custo, profundidade):
        self.estado = estado
        self.pai = pai
        self.custo = custo
        self.profundidade = profundidade
    
class Auxiliar:#Ira auxiliar as buscas
    def expande(self, no, problema, tipo): #Expandira o nó
        Conjfilhos = [] #Conjunto de Filhos
        if(tipo == "cega"):
            possibilidades = problema.acoes(no, tipo) #Possibilidades de filhos
        else:
            possibilidades, conflitos = problema.acoes(no, tipo) #Possibilidades de filhos
        if(possibilidades !=[]):
            for acoes in range(len(possibilidades)): #Caminhos possiveis 
                nofilho = No()
                if(tipo == "cega"):
                    nofilho._init_(possibilidades[acoes],no,no.custo + problema.custo_do_passo, no.profundidade + 1)
                else:
                    nofilho._init_(possibilidades[acoes],no,conflitos, no.profundidade + 1)
                Conjfilhos.append(nofilho) #Adicionando o filhos
        return Conjfilhos

    def matrizprint(self,matriz): #Printar a matriz
        for i in range(len(matriz)):
            for j in range(len(matriz)): 
                print(matriz[i][j], end="")
            print()
        print("\n")

    def caminhos(self, no): #Mostrar o caminho, caso necessario
        caminho = []
        while(no!=None):
            caminho.append(no)
            no = no.pai
        return caminho

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

    def conflitos(self,tabuleiro): #Achar os conflitos indiretos e diretos
        conflitos = copy.deepcopy(tabuleiro)
        for col in range(len(conflitos)): #Coluna por linha
            matriz = copy.deepcopy(tabuleiro)
            matriz = Auxiliar.ColunaX(self,matriz, col)#zera a coluna
            for lin in range(len(conflitos)):
                matriz[lin][col] = "'Q'"#Testar Q's
                Batidas = Auxiliar.detectaQs(self,matriz,lin, col)#Contando as batidas (direta)
                matriz = Auxiliar.ColunaX(self,matriz, col) #Zerar colunas
                aux = copy.deepcopy(matriz) #Matriz auxiliar
                for proxcol in range(len(conflitos)):#Contar as batidas das proximas colunas(indireta)
                    if (proxcol !=col):#Pra ele pular a coluna em que ele está
                        linha = Auxiliar.achaQ(self,aux,proxcol) #Achar o Q da linha
                        Batidas = Batidas + Auxiliar.detectaQs(self,aux,linha, proxcol)
                        aux = Auxiliar.ColunaX(self,aux, proxcol)#Zera a coluna
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