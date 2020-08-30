<h1 align = "center">
<strong>Trabalho de IA 🤖</strong>
</h1>

<p align="center">
   <a href="https://www.linkedin.com/in/josu%C3%A9-batista-694bba135/">
      <img alt="Josué Batista" src="https://img.shields.io/badge/-JosuéBatista-6158f3?style=flat&logo=Linkedin&logoColor=white" />
   </a>
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/Josuebmota/TrabalhoIA?color=6158f3">
  <a href="https://github.com/Josuebmota/TrabalhoIA/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Josuebmota/TrabalhoIA?color=6158f3">
  </a> 
  <a href="https://github.com/Josuebmota/SmallPDV/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-6158f3">
  </a>
  <a href="https://github.com/Josuebmota/TrabalhoIA/stargazers"><img alt="Stargazers" src="https://img.shields.io/github/stars/Josuebmota/TrabalhoIA?color=6158f3&logo=github">
  </a>
</p>

> Trabalho desenvolvido durante a disciplina de inteligência artificial

## 🛠️ Ferramentas e Tecnologias Utilizadas
- [Vs Code](https://code.visualstudio.com/)
- [Python](https://www.python.org/)

## 🚨 Questões
### ♟️ Oito rainhas 
<p align="justify"> O objetivo deste problema é fazer com que o algoritmo posicione oito rainhas em um tabuleiro de xadrez, sem que nenhuma delas ataque as outras. A imagem abaixo mostra os possiveis ataques de uma rainha.</p>
<p align="center">
<img src = "https://user-images.githubusercontent.com/34459397/91664015-b5085a80-eac2-11ea-91d9-207367283980.png" width = 250 height =250/>
</p>
<p align="justify"> Partindo desta diretrizes os algoritmos devem ter à seguinte análise, à medida que a busca vai progredindo de acordo com a coluna em que ele esta, o algoritmo deverá verificar as possibilidades de se colocar uma rainha na coluna posterior. E estas possibilidades sao os filhos do no em que ocorre a análise, que é representado na figura abaixo</p>
<p align="center">
<img src ="https://user-images.githubusercontent.com/34459397/91663952-47f4c500-eac2-11ea-8b20-8ca43ebd9132.png" width = 600 />
</p>

### 🧩 Quebra cabeça de oito peças
<p align="justify">Baseia-se em tabuleiro 3x3, que contém nove peças numeradas de 0 a 8, sendo que a peça vizinha ao quadrado vazio ou zerado, pode deslizar para esta posição. O objetivo deste problema é atingir um estado especificado, como é mostrado na figura abaixo.</p>
<p align = "center">
<img src ="https://user-images.githubusercontent.com/34459397/91663954-4b884c00-eac2-11ea-942b-08caee19cefc.png" width = 300/>
</p>
<p align="justify">A ideia para solucionar essa questão, é de acordo com a movimentação da peça zerada. è ideal que o algoritmo selecionado saiba identificar os possíveis moviemntos de uma posição, e está mobilidae resultará nos filhos do nó, em que ocorre tal verificação, como é mostrado na figura abaixo. Os locais com o plano de fundo cinza representam as posições que o bloco zerado ainda pode acessar.</p>
<p align ="center">
<img src ="https://user-images.githubusercontent.com/34459397/91663947-43301100-eac2-11ea-802d-63e78d28ccb4.png" width = 300 />
</p>

## ⚙️ Algoritmos
Os algoritmos que aplicados ao problema, solucionaram de acordo com as deretrizes.
### 👨‍🦯 Buscas cegas
***1. Busca em profundidade*** - Expande, sempre o nó mais profundo da borda. Quando a profundidade de um ramo chegar ao seu limite, o algoritmo migra para outro ramo. A inlustração abaixo, mostra essa busca aplicado ao problema das 8 rainhas.

<p align ="center">
<img src = "https://user-images.githubusercontent.com/34459397/91664406-7cb64b80-eac5-11ea-9efa-e875fd4ae929.png"/>
</p>

***2. Busca em profundidade com lista de visitados*** - É uma varição da profundidade normal, em que o algoritmo verifica se o nó já foi expandido, evitando os laços infinitos.

***3. Busca em profundidade limitada*** - É especificado até que nível deverá ser aprofundada e após isto, o algoritmo verifica os outros ramos da árvore até deixar a borda vazia ou achar uma solução.

***4. Busca com aprofundamento interativo*** - Utiliza a profundidade limitada de maneira gradativa ate chegar no objetivo. É aplicada para casos de problema de árvores
com profundidade infinita, porem ela não é completa.

***5. Busca em largura*** - E uma solucão em que após o nó raiz ser expandido, os seus nos sucessores irão ser expandidos também e depois os herdeiros destes nós, e assim por diante. A figura seguinte, mostra essa busca aplicado ao problema do puzzle.

<p align ="center">
<img  src = "https://user-images.githubusercontent.com/34459397/91664694-4083ea80-eac7-11ea-9246-92c636b68d21.png"/ width = 500  >
</p>

***6. Busca em custo uniforme*** - Os nos são expandidos de acordo com a ordem do custo, de caminho armazenados dentro dos nos.

### 🚩 Buscas Locais
***1. Hill Climbing*** - É um laço repetitivo que se move de forma constante no sentido do valor factível, ou seja, a medida que as interações ocorrem o resultado tende a ir para o tabuleiro em que os ataques entre as rainhas seja zero. Na figura abaixo, mostra como se dá a resolução do algoritmo aplicado ao problema das oito rainhas. Os números dispostos no tabuleiro representam os ataques de forma direta e indireta de acordo com as suas posicões e os com plano de fundo cinza, são as melhores posições.
<p align = "center">
<img src = "https://user-images.githubusercontent.com/34459397/91665920-5695a900-eacf-11ea-9e7c-d608fe1c56d4.png"/>
</p>

***2. Simulated Annealing*** - Ele evita os mínimos locais, criados no Hill Climbing, porém ele não escolhe o melhor movimento e sim um aleatório, caso a escolha melhorar a situação, ele aceita, mas caso contrário ele seleciona outra opção e assim sucessivamente.

***3. Algoritmos Genéticos*** - Tem como base um conjunto estado, gerados aleatoriamente, chamado de população, que são representados como possíveis disposições das rainhas em um tabuleiro. E a figura abaixo dita as etapas partindo dessa comunidade.

<p align ="center">
<img src = "https://user-images.githubusercontent.com/34459397/91666098-a759d180-ead0-11ea-8662-4208f739b7d2.png" width = 550/>
</p>

## 👁️‍🗨️ Observações
Simulated Annealing e Genéticos, podem apresentar alguns erros, pois estão incompletos

## 🐛 Problemas
Sinta-se a vontade de registrar um novo problema, com um respectivo título e descrição no repositório do [TrabalhoIA](https://github.com/Josuebmota/TrabalhoIA/issues). Se encontrar a solução, avaliarei seu Pull Request.

## 👨‍💻 [](<[https://github.com/Josuebmota/TrabalhoIA](https://github.com/Josuebmota/TrabalhoIA)#autor>)Autores

Criado por [**Josué Batista Mota** ](https://github.com/Josuebmota), <br>esse projeto está sobre [MIT license](./LICENSE) 📃.

Coloque uma ⭐️ caso esse proejto tenha lhe ajudado
