from No import No
from CaracterProblem import Problemas
from Buscas import Buscas
import copy
import time
class Rainhas:

    
    matriz = []
    for l in range(8):
        linha = []
        for c in range(8):
            linha.append("'x'")
        matriz.append(linha)


    def teste_objetivo(self, no):
        matriz = no.estado
        cont = 0
        for l in range(8):
            for c in range(8):
                if (matriz[l][c]=="'Q'"):
                    cont+=1
        if(cont == 8):
            print("Deu bom")
            return True
        return False
    
    def acao(self, no):
        matriz = no.estado
        coluna = no.profundidade
        vetor = []
        for linha in range(8):
            matriz[linha][coluna] = "'Q'"
            #Linha e coluna
            cont = 0
            for l in range(8):
                if(matriz[l][coluna] == matriz[linha][coluna]):
                    cont+=1
                for c in range(8):
                    if(linha == l):
                        if(matriz[linha][c] == matriz[linha][coluna]):
                            cont+=1

            #Principal
            #For seguindo
            c=coluna
            for l in range(linha, 8, 1):
                if(c!=8):
                    if(matriz[linha][coluna] == matriz[l][c]):
                        cont+=1
                    c+=1
            #For voltando
            c = coluna
            for l in range(linha, -1, -1):
                if(c!=-1):
                    if(matriz[linha][coluna] == matriz[l][c]):
                        cont+=1
                    c= c -1

            #Secundaria
            #For voltando
            c= coluna
            for l in range(linha, 8, 1):
                if(c!=-1):
                    if(matriz[linha][coluna] == matriz[l][c]):
                        cont+=1
                    c-=1
            #For seguindo
            c = coluna
            for l in range(linha, -1, -1):
                if(c!=8):
                    if(matriz[linha][coluna] == matriz[l][c]):
                        cont+=1
                    c+=1

            if(cont==6):
                aux = copy.deepcopy(matriz)
                vetor.append(aux)

            matriz[linha][coluna] = "'x'"
        return vetor

    def main(self):
        ini = time.time()
        problema = Problemas()
        problema._init_(self.matriz, self.acao, self.teste_objetivo, 1)
        Buscas.busca_em_largura(self,problema)
        fim = time.time()
        print("Time:", fim - ini)
        return 0


a = Rainhas()
a.main()
    
    
