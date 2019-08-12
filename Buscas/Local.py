from ProblemFeatures import No, Auxiliar
from random import*
import copy
import numpy
from operator import attrgetter

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
        for i in range(1000):
            nSucesso = 0
            for i in range(interacoes):
                if(len(Auxiliar.visitados)==56):
                    break
                Proximo = Auxiliar.Peturbar(self, Nos)
                Delta = Proximo.custo - Nos.custo
                if(Delta<=0 or numpy.exp(-Delta/T)>1):
                    Nos = Proximo
                    Auxiliar.visitados =  []
                    nSucesso +=1
                if(nSucesso>=pulos):
                    break
            T = T*coef
            if(nSucesso==0 or Nos.custo<=0 or T<1):
                break
        Auxiliar.matrizprint(self,Nos.estado)
        print("Profundidade Total:", Nos.profundidade)
        print("Custo:", Nos.custo)
        return Nos

    def Algoritmos_Genéticos(self, n, a,b,c):
        populacao = Local.GerarPopulucao(self, n)
        while(True):
            if(Local.testeGenetico(self,populacao) == True):
                break
            Local.eleicao(self,populacao,n,a)
            populacao = Local.reproducao(self,populacao,n,b,a)
            populacao = Local.mutacao(self,populacao,n,c)
        return populacao
    
    def GerarPopulucao(self, n):
        populacao = []
        for k in range(n):
            matriz = copy.deepcopy(Auxiliar.estado_inicial)
            for col in range(8):
                select = randrange(0,7)
                matriz[select][col]="'Q'"
            Auxiliar.Batidas = Auxiliar.conflitos(self,matriz)
            Individuo = No()
            Individuo._init_(matriz,None,Auxiliar.gerarCusto(self, Auxiliar.Batidas, matriz), None)
            populacao.append(Individuo)
        return populacao

    def testeGenetico(self, populacao):
        populacao.sort(key=attrgetter("custo"))
        if(populacao[0].custo == 1):
            Auxiliar.matrizprint(self,populacao[0].estado)
            print("Profundidade Total:", populacao[0].profundidade)
            print("Custo:", populacao[0].custo)
            return True

    def eleicao(self, populacao,n, porc):
        # while(len(lista)<int(((n*porc)/100))):
        for i in range(int(((n*porc)/100))):
        #     lista.append(copy.deepcopy(populacao[i]))
            a =  randrange(0,len(populacao))
            b =  randrange(0,len(populacao))
            while(b==a):
                b = randrange(0,len(populacao))
            if(populacao[a].custo>=populacao[b].custo):
                del(populacao[a])
            else:
                del(populacao[b])

    def reproducao(self, populacao,n, porc, porc2):
        lista = copy.deepcopy(populacao)
        while(len(lista)<int(((n*porc)/100)+((n*porc2)/100))):
            a = randrange(0,len(lista))
            b = randrange(0,len(lista))
            while(b==a):
                b = randrange(0,len(lista))
            lista1 = copy.deepcopy(Auxiliar.estado_inicial)
            lista2 = copy.deepcopy(Auxiliar.estado_inicial)
            mask = randrange(0,6)
            for col in range(len(lista1)):
                if(col<=mask):
                    lista1[Auxiliar.achaQ(self,lista[a].estado,col)][col] = "'Q'"
                    lista2[Auxiliar.achaQ(self,lista[b].estado,col)][col] = "'Q'"
                else:
                    lista1[Auxiliar.achaQ(self,lista[b].estado,col)][col] = "'Q'"
                    lista2[Auxiliar.achaQ(self,lista[a].estado,col)][col] = "'Q'"
            f1 = Local.expande(self,lista1)
            f2 = Local.expande(self,lista2)
            lista.append(f1)
            lista.append(f2)
        return lista

    def expande(self, lista):
        matriz = copy.deepcopy(lista)
        nofilho = No()
        nofilho._init_(matriz,None,Auxiliar.gerarCusto(self, Auxiliar.conflitos(self,matriz), matriz), None)
        return nofilho

    def mutacao(self, populacao,n, porc):
        lista = copy.deepcopy(populacao)
        for i in range(0, int(((n*porc)/100))):
            p = randrange(0,len(populacao))
            No = copy.deepcopy(lista[p])
            c = randrange(0,7)
            linha = Auxiliar.achaQ(self, No.estado, c)
            l = randrange(0,7)
            No.estado[linha][c] = "'x'"
            No.estado[l][c] = "'Q'"
            No.custo = Auxiliar.gerarCusto(self,Auxiliar.conflitos(self,No.estado), No.estado)
            lista.append(No)
        return lista