class Problema: #Caracteristicas do problema que será executado
    def _init_(self, estado_inicial, acoes, teste_objetivo, custo_do_passo):
        self.estado_inicial = estado_inicial
        self.acoes = acoes
        self.teste_objetivo = teste_objetivo
        self.custo_do_passo = custo_do_passo

class No: #Caracteristicas da Posicao
    def _init_(self, estado, pai, custo_do_caminho, profundidade):
        self.estado = estado
        self.pai = pai
        self.custo_do_caminho = custo_do_caminho
        self.profundidade = profundidade
    
class Auxiliar:
    def expande(self, no, problema, tipo): #Expandira o nó
        Conjfilhos = [] #Conjunto de Filhos
        possibilidades = problema.acoes(no, tipo) #Possibilidades de filhos
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

    def caminhos(self, no): #Mostrar o caminho, caso necessario
        caminho = []
        while(no!=None):
            caminho.append(no)
            no = no.pai
        return caminho
