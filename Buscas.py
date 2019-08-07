from ProblemFeatures import No
import random
from operator import attrgetter
from random import randrange

class Buscas: #Bucas separadas por funções

    def expande(self, no, problema, tipo): #Expandira o nó
        Conjfilhos = [] #Conjunto de Filhos
        possibilidades = problema.acoes(no, tipo) #Possibilidades de filhos
        if(possibilidades !=[]):
            for acoes in range(len(possibilidades)): #Caminhos possiveis 
                nofilho = No()
                nofilho._init_(possibilidades[acoes],no,no.custo_do_caminho + problema.custo_do_passo, no.profundidade + 1)
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

    def busca_em_profundidade(self,problema):
        borda = [] #Lista de Nos
        Nos = No()
        Nos._init_(problema.estado_inicial,None, 0, 0) #No inicial
        borda.insert(0,Nos) #Inserindo
        while(True):
            Buscas.matrizprint(self,borda[0].estado)
            if(problema.teste_objetivo(borda[0],"normal") == True ):#Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Buscas.caminhos(self,borda[0])
            filhos = Buscas.expande(self,borda[0], problema,"normal") #Expandir
            random.shuffle(filhos) #Bagunçar a lista de filhos
            borda.pop(0)#remover da borda
            for acoes in range(len(filhos)):
                 borda.insert(0,filhos[acoes]) #Inserir no começo
    
    def busca_em_largura(self, problema):
        borda = [] #Lista de Nos
        Nos = No()
        Nos._init_(problema.estado_inicial,None, 0, 0) #No inicial
        borda.insert(0,Nos) #Inserindo
        while(True):
            Buscas.matrizprint(self,borda[0].estado)
            if(problema.teste_objetivo(borda[0],"normal") == True ):#Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Buscas.caminhos(self,borda[0])
            filhos = Buscas.expande(self,borda[0], problema,"normal") #Expandir
            #random.shuffle(filhos) #Bagunçar a lista de filhos
            borda.pop(0)#remover da borda
            for acoes in range(len(filhos)):
                 borda.append(filhos[acoes])#Inserir no final
       

    def busca_em_profundidade_limitada(self, problema,limite):
        borda = [] #Lista de Nos
        Nos = No()
        Nos._init_(problema.estado_inicial,None, 0, 0) #No inicial
        borda.insert(0,Nos) #Inserindo
        while(True):
            if(borda==[]):
                print("Não foi atingido neste limite")
                return 0, False #Boolean usado na busca interativa
            Buscas.matrizprint(self,borda[0].estado)
            if(problema.teste_objetivo(borda[0],"normal") == True ): #Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Buscas.caminhos(self,borda[0]), True #Boolean usado na busca interativa
            if(borda[0].profundidade<limite): #So ira adicionar novos filhos caso chegue no limite
                filhos = Buscas.expande(self,borda[0], problema,"normal") #Expandir
                random.shuffle(filhos) #Bagunçar a lista de filhos
                borda.pop(0) #remover da borda
                for acoes in range(len(filhos)):
                    borda.insert(0,filhos[acoes])
            else:
                borda.pop(0)
    
    def busca_em_aprofundamento_interativo(self, problema):
        interacao = 0 #Número de interações
        while(True):#Fica em um laço até achar a solução
            caminho, resultado = Buscas.busca_em_profundidade_limitada(self,problema, interacao)
            interacao+=1
            if(resultado == True):
                return caminho
            print("-----------------------------------------------")
    
    def busca_em_profundidade_com_lista_de_visitados(self,problema):
        borda = [] #Lista de Nos
        visitado = []
        Nos = No()
        Nos._init_(problema.estado_inicial,None, 0, 0) #No inicial
        borda.insert(0,Nos) #Inserindo
        while(True):
            Buscas.matrizprint(self,borda[0].estado) 
            if(borda==[]):
                print("Profundidade Total:", borda[0].profundidade)
                return Buscas.caminhos(self,borda[0])
            if(problema.teste_objetivo(borda[0],"normal") == True ):#Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Buscas.caminhos(self,borda[0])
            while(True): #Fica em um laço eliminado os visitados
                if not borda[0] in visitado:
                    visitado.append(borda[0])
                    break
                borda.pop(0)
            filhos = Buscas.expande(self,borda[0], problema,"normal") #Expandir
            random.shuffle(filhos) #Bagunçar a lista de filhos
            borda.pop(0)
            for acoes in range(len(filhos)):
                 borda.insert(0,filhos[acoes]) #Inserir no começo
    
    def busca_com_custo_uniforme(self, problema):
        borda = [] #Lista de Nos
        Nos = No()
        Nos._init_(problema.estado_inicial,None, 0, 0) #No inicial
        borda.insert(0,Nos) #Inserindo
        while(True):
            Buscas.matrizprint(self,borda[0].estado)
            if(problema.teste_objetivo(borda[0],"normal") == True ):#Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Buscas.caminhos(self,borda[0])
            filhos = Buscas.expande(self,borda[0], problema,"normal") #Expandir
            borda.sort(key=attrgetter("custo_do_caminho"))
            borda.pop(0)
            for acoes in range(len(filhos)):
                 borda.append(filhos[acoes])#Inserir no final

    def Hill_Climbing(self, problema): #Subida da encosta
        matriz = [["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"],
                  ["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"],
                  ["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"],
                  ["'x'","'x'","'x'","'Q'","'x'","'x'","'x'","'x'"],
                  ["'Q'","'x'","'x'","'x'","'Q'","'x'","'x'","'x'"],
                  ["'x'","'Q'","'x'","'x'","'x'","'Q'","'x'","'Q'"],
                  ["'x'","'x'","'Q'","'x'","'x'","'x'","'Q'","'x'"],
                  ["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"]]
        # matriz = problema.estado_inicial # Gerar matriz automatica
        # for c in range(len(matriz)):
        #     n= randrange(0,7)
        #     matriz[n][c] = "'Q'"
        Nos = No()
        Nos._init_(matriz,None, 0, 0) #No inicial
        while(True):
            Buscas.matrizprint(self,Nos.estado)
            if(problema.teste_objetivo(Nos,"sa") == True ):
                print("Profundidade Total:", Nos.profundidade)
                return Buscas.caminhos(self,Nos)
            Proximo = Buscas.expande(self,Nos, problema,"o") #Expandir
            Nos = Proximo[0]
    
    def Simulated_Annealing(self, problema): #Recozimento Simulado
        return 0

    def Algoritmos_Genéticos(self, problema):
        return 0   
