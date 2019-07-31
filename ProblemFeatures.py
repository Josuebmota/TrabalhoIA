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
    
    def getPai(self):
        return self.pai
    def setPai(self, pai):
        self.pai = pai

    def getEstado(self):
        return self.estado
    def setEstado(self, estado):
        self.estado = estado

    def getCusto(self):
        return self.custo_do_caminho
    def setCusto(self, custo_do_caminho):
        self.custo_do_caminho = custo_do_caminho
        
    def getProfundidade(self):
        return self.profundidade
    def setProfundidade(self, profundidade):
        self.profundidade=profundidade 
