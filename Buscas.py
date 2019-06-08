from No import No
from CaracterProblem import Problemas
import random

class Buscas:
    #Vai expandir o no

    def expande(self, no, problema):
        Conjfilhos = [] #Conjunto de Filhos
        possibilidades = problema.acoes(no) #Possibilidades de filhos
        if(possibilidades !=[]):
            for acoes in range(len(possibilidades)): #Caminhos possiveis 
                nofilho = No()
                nofilho._init_(possibilidades[acoes],no,no.custo_do_caminho + problema.custo_do_passo, no.profundidade + 1)
                Conjfilhos.append(nofilho) #Adicionando o filhos
        return Conjfilhos

    def matrizprint(self,matriz): #Printar a matriz
        for i in range(8):
            for j in range(8): 
                print(matriz[i][j], end="")
            print()
        print("\n")

    def busca_em_profundidade(self,problema):
        borda = [] #Lista de Nos
        Nos = No()
        Nos._init_(problema.estado_inicial,None, 0, 0) #No inicial
        borda.insert(0,Nos) #Inserindo
        while(True):
            Buscas.matrizprint(self,borda[0].estado)
            if(problema.teste_objetivo(borda[0]) == True ):#Atingir o objetivo
                break
            filhos = Buscas.expande(self,borda[0], problema) #Expandir
            random.shuffle(filhos) #Bagunçar a lista de filhos
            borda.pop(0)
            for acoes in range(len(filhos)):
                 borda.insert(0,filhos[acoes]) #Inserir no começo
    
    def busca_em_largura(self, problema):
        borda = [] #Lista de Nos
        Nos = No()
        Nos._init_(problema.estado_inicial,None, 0, 0) #No inicial
        borda.insert(0,Nos) #Inserindo
        while(True):
            Buscas.matrizprint(self,borda[0].estado)
            if(problema.teste_objetivo(borda[0]) == True ):#Atingir o objetivo
                break
            filhos = Buscas.expande(self,borda[0], problema) #Expandir
            random.shuffle(filhos) #Bagunçar a lista de filhos
            borda.pop(0)
            for acoes in range(len(filhos)):
                 borda.append(filhos[acoes])#Inserir no final

    def busca_em_profundidade_limitada(self, problema,limite):
        borda = []
        Nos = No()
        Nos._init_(problema.estado_inicial,None, 0, 0)
        borda.insert(0,Nos)
        while(borda[0].profundidade!=limite+1):
            Buscas.matrizprint(self,borda[0].estado)
            if(problema.teste_objetivo(borda[0]) == True ):
                return 0
            filhos = Buscas.expande(self,borda[0], problema)
            random.shuffle(filhos)
            borda.pop(0)
            for acoes in range(len(filhos)):
                 borda.insert(0,filhos[acoes])
           
        print("Nao atingiu o objetivo neste limite")
        return False
    
    def busca_em_aprofundamento_interativo(self, problema, profundidade):
        for i in range(profundidade+1):
            Buscas.busca_em_profundidade_limitada(self,problema, i)
            print("-----------------------------------------------")
        return 0
    
    def busca_com_custo_uniforme(self, problema):
        borda = [] #Lista de Nos
        Nos = No()
        Nos._init_(problema.estado_inicial,None, 0, 0) #No inicial
        borda.insert(0,Nos) #Inserindo
        while(True):
            Buscas.matrizprint(self,borda[0].estado)
            if(problema.teste_objetivo(borda[0]) == True ):#Atingir o objetivo
                print(borda[0].custo_do_caminho)
                break
            filhos = Buscas.expande(self,borda[0], problema) #Expandir
            random.shuffle(filhos)
            borda.pop(0)
            for acoes in range(len(filhos)):
                 borda.append(filhos[acoes])#Inserir no final