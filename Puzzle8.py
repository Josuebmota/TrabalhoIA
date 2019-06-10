from No import No
from CaracterProblem import Problemas
from Buscas import Buscas
import copy
import time

class Puzzle8:

    tabuleiro = [[7,2,4],[5,0,6],[8,3,1]]

    def teste_objetivo(self, no):
        objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        if(no.estado == objetivo):
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
        problema._init_(self.tabuleiro, self.acao, self.teste_objetivo, 1)
        Buscas.busca_em_largura(self,problema)
        fim = time.time()
        print("Time:", fim - ini)
        return 0

a = Puzzle8()
a.main()