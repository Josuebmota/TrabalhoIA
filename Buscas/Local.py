from ProblemFeatures import No, Auxiliar
from random import*
import copy
import numpy

class Local:
   
    def Hill_Climbing(self): #Subida da encosta
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
        Auxiliar.Batidas = Auxiliar.conflitos(self, matriz)
        Nos = No()
        Nos._init_(matriz,None,Auxiliar.gerarCusto(self, Auxiliar.Batidas, matriz), 0) #No inicial
        for i in range(1000):
            if(Nos.custo<=0):
                break
            Nos = Auxiliar.expandelocal(self, Nos)
        Auxiliar.matrizprint(self,Nos.estado)
        print("Profundidade Total:", Nos.profundidade)
        return Auxiliar.caminhos(self,Nos)

    def Simulated_Annealing(self,T,interacoes, pulos, coef): #Recozimento Simulado
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
        Auxiliar.Batidas = Auxiliar.conflitos(self, matriz)
        Nos = No()
        Nos._init_(matriz,None,Auxiliar.gerarCusto(self, Auxiliar.Batidas, matriz), 0) #No inicial
        Auxiliar.matrizprint(self,Nos.estado)
        for i in range(5000):
            nSucesso = 0
            for i in range(interacoes):
                if(len(Auxiliar.visitados)==56):
                    break
                Proximo = Auxiliar.Peturbar(self, Nos)
                Delta = Proximo.custo - Nos.custo
                if(Delta<=0 or numpy.exp(-Delta/T)>1):
                    Nos = Proximo
                    Auxiliar.visitados =  []
                    Auxiliar.matrizprint(self,Nos.estado)
                    nSucesso +=1
                if(nSucesso>=pulos):
                    break
            T = T*coef
            if(nSucesso==0 or Nos.custo<=0):
                break
        Auxiliar.matrizprint(self,Nos.estado)
        print("Profundidade Total:", Nos.profundidade)
        print("Custo:", Nos.custo)
        Local.visitados =[]
        return Nos

    def Algoritmos_Genéticos(self, problema):
        cromossomo = [1,3,4,2,5,6,7,0]
        Populacao = Local.GerarPopulucao(self,cromossomo)
        while(True):
            if(Local.testegenetico == True):
                break
            Populacao = Local.eleicao(self,Populacao)
            Populacao = Local.reproducao(self,Populacao)
            Populacao = Local.mutacao(self,Populacao)
    
    def eleicao(self, populacao):
        lista = []
        p1 = randrange(0,len(populacao))
        p2 = randrange(0,len(populacao))
        while(p2==p1):
            p2 = randrange(0,len(populacao))
        lista.append(populacao[p1])
        lista.append(populacao[p2])
        return lista

    def reproducao(self, populacao):
        lista = copy.deepcopy(populacao)
        while(True):
            if(len(lista)>=16):
                return lista
            a = randrange(0,len(lista))
            b = randrange(0,len(lista))
            while(b==a):
                b = randrange(0,len(lista))
            lista1 = []
            lista2 = []
            mask = Auxiliar.selectMask(self)
            for i in range(len(mask)):
                if(mask[i]==0):
                    lista1.append(lista[a][i])
                    lista2.append(lista[b][i])
                if(mask[i]==1):
                    lista1.append(lista[b][i])
                    lista2.append(lista[a][i])
            lista.append(lista1)
            lista.append(lista2)
    