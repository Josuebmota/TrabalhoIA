from ProblemFeatures import No, Auxiliar
import random
from operator import attrgetter
from random import randrange

class Cega: #Bucas separadas por funções

    def busca_em_profundidade(self,problema):
        borda = [] #Lista de Nos
        Nos = No()
        Nos._init_(problema.estado_inicial,None, 0, 0) #No inicial
        borda.insert(0,Nos) #Inserindo
        while(True):
            Auxiliar.matrizprint(self,borda[0].estado)
            if(problema.teste_objetivo(borda[0],"cega") == True ):#Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Auxiliar.caminhos(self,borda[0])
            filhos = Auxiliar.expande(self,borda[0], problema,"cega") #Expandir
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
            Auxiliar.matrizprint(self,borda[0].estado)
            if(problema.teste_objetivo(borda[0],"cega") == True ):#Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Auxiliar.caminhos(self,borda[0])
            filhos = Auxiliar.expande(self,borda[0], problema,"Cega") #Expandir
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
            Auxiliar.matrizprint(self,borda[0].estado)
            if(problema.teste_objetivo(borda[0],"cega") == True ): #Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Auxiliar.caminhos(self,borda[0]), True #Boolean usado na busca interativa
            if(borda[0].profundidade<limite): #So ira adicionar novos filhos caso chegue no limite
                filhos = Auxiliar.expande(self,borda[0], problema,"cega") #Expandir
                random.shuffle(filhos) #Bagunçar a lista de filhos
                borda.pop(0) #remover da borda
                for acoes in range(len(filhos)):
                    borda.insert(0,filhos[acoes])
            else:
                borda.pop(0)
    
    def busca_em_aprofundamento_interativo(self, problema):
        interacao = 0 #Número de interações
        while(True):#Fica em um laço até achar a solução
            caminho, resultado = Cega.busca_em_profundidade_limitada(self,problema, interacao)
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
            Auxiliar.matrizprint(self,borda[0].estado) 
            if(borda==[]):
                print("Profundidade Total:", borda[0].profundidade)
                return Auxiliar.caminhos(self,borda[0])
            if(problema.teste_objetivo(borda[0],"cega") == True ):#Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Auxiliar.caminhos(self,borda[0])
            while(True): #Fica em um laço eliminado os visitados
                if not borda[0] in visitado:
                    visitado.append(borda[0])
                    break
                borda.pop(0)
            filhos = Auxiliar.expande(self,borda[0], problema,"cega") #Expandir
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
            Auxiliar.matrizprint(self,borda[0].estado)
            if(problema.teste_objetivo(borda[0],"cega") == True ):#Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Auxiliar.caminhos(self,borda[0])
            filhos = Auxiliar.expande(self,borda[0], problema,"cega") #Expandir
            borda.sort(key=attrgetter("custo_do_caminho"))
            borda.pop(0)
            for acoes in range(len(filhos)):
                 borda.append(filhos[acoes])#Inserir no final