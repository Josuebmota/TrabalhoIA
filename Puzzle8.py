from No import No
from CaracterProblem import Problemas
from Buscas import Buscas
import copy
import time

class Puzzle8:
    
    def estado_inicial(self):
        problema = Problemas()
        problema._init_([[0, 1, 2], [3, 4, 5], [6, 7, 8]], self.acao, self.teste_inicial,1)
        resultado = Buscas.busca_em_profundidade_limitada(self,problema, 20) 
        print(resultado[0].estado)
        return resultado[0].estado

    def teste_inicial(self, no):
        if(no.estado ==  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
            return True
        return False

    def teste_objetivo(self, no):
        if(no.estado ==  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]):
            return True
        return False

    def acao(self, no):
        l= 0
        c= 0 
        puzzle = no.estado
        vetor = []
        for i in range(3):
            for j in range(3):
                if(puzzle[i][j]==0):
                    l=i
                    c=j

        #mover para direita
        if(c!=2):   
            aux = copy.deepcopy(puzzle)
            aux[l][c] = puzzle[l][c+1]
            aux[l][c+1] = puzzle[l][c]
            vetor.append(aux)
        #mover para esquerda
        if(c!=0):
            aux = copy.deepcopy(puzzle)
            aux[l][c] = puzzle[l][c-1]
            aux[l][c-1] = puzzle[l][c]
            vetor.append(aux)
        #mover para cima
        if(l!=0):
            aux = copy.deepcopy(puzzle)
            aux[l][c] = puzzle[l-1][c]
            aux[l-1][c] = puzzle[l][c]
            vetor.append(aux)
        #mover para baixo
        if(l!=2):
            aux = copy.deepcopy(puzzle)
            aux[l][c] = puzzle[l+1][c]
            aux[l+1][c] = puzzle[l][c]
            vetor.append(aux)
        return vetor 

    def main(self):
        ini = time.time()
        problema = Problemas()
        problema._init_(self.estado_inicial(), self.acao, self.teste_objetivo, 1)
        Buscas.busca_em_largura(self,problema)
        fim = time.time()
        print("Time:", fim - ini)
        return 0

a = Puzzle8()
a.main()