class Problemas:
    def _init_(self, estado_inicial, acoes, teste_objetivo, custo_do_passo):
        self.estado_inicial = estado_inicial
        self.acoes = acoes
        self.teste_objetivo = teste_objetivo
        self.custo_do_passo = custo_do_passo


#definir as ações: direita, esqueda, baixo e cima
#Teste objetivo do problema
#Estado inicial