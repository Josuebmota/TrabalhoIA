from ProblemFeatures import Problema
from Buscas.Cega import Cega
from Buscas.Local import Local
from Problemas.Puzzle8 import Puzzle8
from Problemas.Rainhas import Rainhas
import time


class Main:
    def executar(self):
        ini = time.time() #Tempo
        Select = Rainhas() #Selecionar qual o problema será resolvido
        #Montando o problema com os atributos do problema
        problema = Problema()
        problema._init_(Select.estado_inicial, Select.acao, Select.teste_objetivo, 1)
        #Selecionar o tipo de busca, Cega ou local
        #Caso for busca com profundidade limitada, é preciso especificar o limite no parametro
        #Buscas locais so podem ser usadas nas Rainhas
        # caminho = Cega.busca_em_profundidade(self, problema)
        caminho = Local.Hill_Climbing(self, problema)
        fim = time.time()
        print("Time:", fim - ini)
        return caminho #Retornar o caminho percorrido

#Executar as tarefas
Exe = Main()
Exe.executar()