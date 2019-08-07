from ProblemFeatures import No, Auxiliar
import random
from random import randrange

class Local:
    
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
            Auxiliar.matrizprint(self,Nos.estado)
            if(problema.teste_objetivo(Nos,"local") == True ):
                print("Profundidade Total:", Nos.profundidade)
                return Auxiliar.caminhos(self,Nos)
            Proximo = Auxiliar.expande(self,Nos, problema,"o") #Expandir
            Nos = Proximo[0]
    
    def Simulated_Annealing(self, problema): #Recozimento Simulado
        return 0

    def Algoritmos_Genéticos(self, problema):
        return 0 