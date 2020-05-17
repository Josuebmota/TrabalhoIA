class Auxiliar:#Ira auxiliar as buscas
    #--------------------------Auxilia nas Buscas sem informação-----------------------------------
    def expande(self, no, problema, tipo): #Expandira o nó
        Conjfilhos = [] #Conjunto de Filhos
        possibilidades = problema.acoes(no, tipo) #Possibilidades de filhos
        if(possibilidades !=[]):
            for acoes in range(len(possibilidades)): #Caminhos possiveis 
                nofilho = No()
                nofilho._init_(possibilidades[acoes],no,no.custo + problema.custo_do_passo, no.profundidade + 1)
                Conjfilhos.append(nofilho) #Adicionando o filhos
        return Conjfilhos
    
    estado_inicial = [] # gerar matriz inicial
    indice = 8
    for l in range(indice):
        linha = []
        for c in range(indice):
            linha.append("'x'")
        estado_inicial.append(linha)
    
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

    def detectaQs(self, auxMatriz, linha, coluna): #Funcao para detectar se tem ataques
        cont = 0
        for l in range(len(auxMatriz)):
            if(auxMatriz[l][coluna] == auxMatriz[linha][coluna]):
                cont+=1
            for c in range(len(auxMatriz)):
                if(linha == l):
                    if(auxMatriz[linha][c] == auxMatriz[linha][coluna]):
                        cont+=1

        #Principal
        #For seguindo
        c=coluna
        for l in range(linha,len(auxMatriz), 1):
            if(c!=len(auxMatriz)):
                if(auxMatriz[linha][coluna] == auxMatriz[l][c]):
                    cont+=1
                c+=1
        #For voltando
        c = coluna
        for l in range(linha, -1, -1):
            if(c!=-1):
                if(auxMatriz[linha][coluna] == auxMatriz[l][c]):
                    cont+=1
                c-=1
        #Secundaria
        #For voltando
        c= coluna
        for l in range(linha, len(auxMatriz), 1):
            if(c!=-1):
                if(auxMatriz[linha][coluna] == auxMatriz[l][c]):
                    cont+=1
                c-=1
        #For seguindo
        c = coluna
        for l in range(linha, -1, -1):
            if(c!=len(auxMatriz)):
                if(auxMatriz[linha][coluna] == auxMatriz[l][c]):
                    cont+=1
                c+=1
        return cont-6
    
    #--------------------------Auxilia nas Buscas Locais-----------------------------------
    def achaQ(self, matriz, col): #Funcao para achar a linha da rainha
        for linha in range(len(matriz)):
            if (matriz[linha][col]=="'Q'"):
                return linha
                
    def ColunaX(self, matriz, coluna): #Funcao para deletar uma coluna
        for linha in range(len(matriz)):
            matriz[linha][coluna]= "'x'"
        return matriz

    def conflitos(self,tabuleiro): #Achar os conflitos indiretos e diretos
        conflitos = copy.deepcopy(tabuleiro)
        for col in range(len(conflitos)): #Coluna por linha
            matriz = copy.deepcopy(tabuleiro)
            matriz = Auxiliar.ColunaX(self,matriz, col)#zera a coluna
            for lin in range(len(conflitos)):
                matriz[lin][col] = "'Q'"#Testar Q's
                Batidas = Auxiliar.detectaQs(self,matriz,lin, col)#Contando as batidas (direta)
                matriz = Auxiliar.ColunaX(self,matriz, col) #Zerar colunas
                aux = copy.deepcopy(matriz) #Matriz auxiliar
                for proxcol in range(len(conflitos)):#Contar as batidas das proximas colunas(indireta)
                    if (proxcol !=col):#Pra ele pular a coluna em que ele está
                        linha = Auxiliar.achaQ(self,aux,proxcol) #Achar o Q da linha
                        Batidas = Batidas + Auxiliar.detectaQs(self,aux,linha, proxcol)
                        aux = Auxiliar.ColunaX(self,aux, proxcol)#Zera a coluna
                conflitos[lin][col] = Batidas#Matriz de batidas
                Batidas=0
        return conflitos

    def melhorfilho(self,matriz):#Colocar os melhores filhos na lista
        menor = 100
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if(menor>matriz[i][j]):
                    menor=matriz[i][j]
        liMenor=[]
        for i in range(len(matriz)):
            for j in  range(len(matriz)):
                if(matriz[i][j]==menor):
                    liMenor.append(matriz[i][j])
        return liMenor, menor

    def gerarCusto(self,conflitos, matriz):
        return conflitos[Auxiliar.achaQ(self,matriz,0)][0]

    def vizinhos(self, matriz):
        vizinhos =[]
        for i in range(len(matriz)):
            for j in  range(len(matriz)):
                if(matriz[i][j]!="'Q'"):
                    aux = copy.deepcopy(matriz)
                    aux = Auxiliar.ColunaX(self,aux,j)
                    aux[i][j]="'Q'"
                    vizinhos.append(aux)
        return vizinhos

    Batidas = []
    visitados = []

    def expandelocal(self, no):
        aux = copy.deepcopy(no.estado)
        liMenor, menor = Auxiliar.melhorfilho(self,Auxiliar.Batidas)#Melhor filho
        select = randrange(0,len(liMenor))#Selecionar um dos melhores filhos
        contador = -1
        for i in range(len(aux)):
            for j in range(len(aux)):
                if(menor == Auxiliar.Batidas[i][j]):#Procurar o melhor filho selecionado
                    contador+=1 #Depende da quantiadade de melhores filhos
                if(contador==select):#Achou
                    linha = Auxiliar.achaQ(self,aux,j)#Pega linha em que a rainha está
                    aux[linha][j] = "'x'" #Faz a troca
                    aux[i][j] = "'Q'"
                    Auxiliar.Batidas = Auxiliar.conflitos(self,aux)
                    nofilho = No()
                    nofilho._init_(aux,no,Auxiliar.gerarCusto(self, Auxiliar.Batidas, aux), no.profundidade + 1)
                    return nofilho

    def Peturbar(self, no):
        vizinhos = Auxiliar.vizinhos(self,no.estado)
        while(True):
            select = randrange(0,len(vizinhos))
            if(not vizinhos[select] in Auxiliar.visitados):
                Auxiliar.visitados.append(vizinhos[select])
                break
        Proximo = No()
        Proximo._init_(vizinhos[select],no,Auxiliar.gerarCusto(self, Auxiliar.conflitos(self,vizinhos[select]),vizinhos[select]),no.profundidade + 1)
        return Proximo

    def selectMask(self):
        a = randrange(0,2)
        if(a==0):
            return [0,0,0,0,1,1,1,1]
        if(a==1):
            return [1,1,1,0,0,0,0,0]
        if(a==2):
            return [1,1,0,0,0,0,1,1]