# Implementação de Algoritmos para encontrar os caminhos mínimos 
A primeira parte desta atividade consiste em criar um programa para ler os arquivos de bases de dados e armazenar em uma estrutura de dados (da nossa escolha) em qualquer linguagem de programação. Depois iremos implementar algoritmos para encontrar os caminhos mínimos para cada base de dados. Consideramos as bases: ATT48, DANTZIG42, FRI26, GR17 e P01 [disponíveis no link](https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html).
## Descrição 
Esta atividade é continuação do Trabalho prático da AB1 e consiste em implementar algumas soluções para o PCV. Cada membro da equipe ficará responsavel por implementar um dos algoritmos abaixo:

**O algoritmo de força bruta para o PCV e executar para todas as bases de dados indicadas.**
sys: Permite interagir com o sistema (ex: ler argumentos da linha de comando, encerrar o programa).
requests: Facilita o envio de requisições HTTP para interagir com a web de maneira simples e direta.
itertools.permutations: Gera todas as permutações possíveis de um conjunto de elementos, útil para resolver problemas de combinação e permutação.

**O algoritmo de Dijkstra adaptado para o PCV e executar para todas as bases de dados indicadas.**
Este código Python implementa o algoritmo de Dijkstra para resolver o Problema do Caixeiro Viajante (TSP). Para executá-lo, instale as bibliotecas heapq, pandas, requests e io. Depois, selecione uma base de dados entre seis opções disponíveis. O algoritmo encontrará a rota mais curta entre as cidades da base de dados escolhida e imprimirá o caminho encontrado, juntamente com o custo total da rota.

- O algoritmo de AGM ( [Kruskal](https://github.com/thascript/AtividadeGrafos/tree/main/kruskal) ou Prim) para obter um limite inferior para a solução do problema do caixeiro viajante.
  
**O Algoritmo de Christofides para o PCV**




## Instalação

**Algoritmo de Christofides** , você precisa ter as seguintes dependências instaladas:

- NetworkX: Biblioteca Python para criação, manipulação e estudo de redes complexas.
  Instalação via pip: ```pip install networkx```

- Requests: Biblioteca Python para fazer solicitações HTTP.
Instalação via pip: ``` pip install requests```

**Algoritmo de força bruta**, você precisa ter as seguintes dependências instaladas:
Importações:
- import sys:
- import requests
- from itertools import permutations

Explicação:
sys: Permite interagir com o sistema (ex: ler argumentos da linha de comando, encerrar o programa).
requests: Facilita o envio de requisições HTTP para interagir com a web de maneira simples e direta.
itertools.permutations: Gera todas as permutações possíveis de um conjunto de elementos, útil para resolver problemas de combinação e permutação.
## Como Usar
Para implementaçao do algoritmo de Kruskal nao foi necessário nenhuma dependencia externa além das bibliotecas importatdas que se apresentam no arquivo.

## Contato do desenvolvedor
Nome e e-mail do(s) desenvolvedor(es):
- Douglas Alves: felipe.douglas.alves@hotmail.com
- Josué Junior: josue.junior@arapiraca.ufal.br
- Maria Izabel: maria.franca1@arapiraca.ufal.br
- Thalia Oliveira: thalia.oliveira@arapiraca.ufal.br

## Hardware sugerido
A configuração do sistema inclui um processador Ryzen 5 da série 7000, 8 GB de RAM e um SSD de 521 GB. O processador opera a 2.6 GHz e o sistema operacional foi Windowns10.
Software necessário: Todo o projeto está rodando no Colab.
