from No import No
from CaracterProblem import Problemas
import random
from operator import attrgetter

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
        for i in range(len(matriz)):
            for j in range(len(matriz)): 
                print(matriz[i][j], end="")
            print()
        print("\n")

    def caminhos(self, no):
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
            if(problema.teste_objetivo(borda[0]) == True ):#Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Buscas.caminhos(self,borda[0])
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
                print("Profundidade Total:", borda[0].profundidade)
                return Buscas.caminhos(self,borda[0])
            filhos = Buscas.expande(self,borda[0], problema) #Expandir
            #random.shuffle(filhos) #Bagunçar a lista de filhos
            borda.pop(0)
            for acoes in range(len(filhos)):
                 borda.append(filhos[acoes])#Inserir no final
       

    def busca_em_profundidade_limitada(self, problema,limite):
        borda = []
        Nos = No()
        Nos._init_(problema.estado_inicial,None, 0, 0)
        borda.insert(0,Nos)
        while(True):
            Buscas.matrizprint(self,borda[0].estado)
            if(borda==[]):
                print("Profundidade Total:", borda[0].profundidade)
                return Buscas.caminhos(self,borda[0])
            if(problema.teste_objetivo==borda[0]):
                print("Profundidade Total:", borda[0].profundidade)
                return Buscas.caminhos(self,borda[0])
            if(borda[0].profundidade!=limite+1):
                filhos = Buscas.expande(self,borda[0], problema)
                random.shuffle(filhos)
                for acoes in range(len(filhos)):
                    borda.insert(0,filhos[acoes])
            borda.pop(0)
    
    def busca_em_aprofundamento_interativo(self, problema, interacao):
        interacao = 0
        while(True):
            resultado = Buscas.busca_em_profundidade_limitada(self,problema, interacao)
            interacao+=1
            if(resultado == True):
                break
            print("-----------------------------------------------")
        return 0
    
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
            if(problema.teste_objetivo(borda[0]) == True ):#Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Buscas.caminhos(self,borda[0])
            while(True):
                if not borda[0] in visitado:
                    visitado.append(borda[0])
                    break
                borda.pop(0)
            filhos = Buscas.expande(self,borda[0], problema) #Expandir
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
            if(problema.teste_objetivo(borda[0]) == True ):#Atingir o objetivo
                print("Profundidade Total:", borda[0].profundidade)
                return Buscas.caminhos(self,borda[0])
            filhos = Buscas.expande(self,borda[0], problema) #Expandir
            borda.sort(key=attrgetter("custo_do_caminho"))
            borda.pop(0)
            for acoes in range(len(filhos)):
                 borda.append(filhos[acoes])#Inserir no final
