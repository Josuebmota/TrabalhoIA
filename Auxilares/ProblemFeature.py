import copy
from random import*
class Problema: #Caracteristicas do problema que será executado
    def _init_(self, estado_inicial, acoes, teste_objetivo, custo_do_passo):
        self.estado_inicial = estado_inicial
        self.acoes = acoes
        self.teste_objetivo = teste_objetivo
        self.custo_do_passo = custo_do_passo

class No: #Caracteristicas da Posicao
    def _init_(self, estado, pai, custo, profundidade):
        self.estado = estado
        self.pai = pai
        self.custo = custo
        self.profundidade = profundidade
    
