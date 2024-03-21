# Implementação de Algoritmos para encontrar os caminhos mínimos 
A primeira parte desta atividade consiste em criar um programa para ler os arquivos de bases de dados e armazenar em uma estrutura de dados (da nossa escolha) em qualquer linguagem de programação. Depois iremos implementar algoritmos para encontrar os caminhos mínimos para cada base de dados. Consideramos as bases: ATT48, DANTZIG42, FRI26, GR17 e P01 [disponíveis no link](https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html).
## Descrição 
Esta atividade é continuação do Trabalho prático da AB1 e consiste em implementar algumas soluções para o PCV. Cada membro da equipe ficará responsavel por implementar um dos algoritmos abaixo e executar para todas as bases de dados indicadas acima:

**O algoritmo de força bruta para o PCV**
Este algoritmo gera todas as permutações possíveis de visitas às cidades, calcula o custo total para cada rota, e seleciona a rota com o menor custo como a solução ótima. Apesar de garantir a resposta mais eficiente, sua complexidade exponencial torna o método inviável para um grande número de cidades, devido ao aumento exorbitante do tempo de processamento e recursos necessários.

**O algoritmo de Dijkstra adaptado para o PCV**
 O algoritmo encontrará a rota mais curta entre as cidades da base de dados escolhida e imprimirá o caminho encontrado, juntamente com o custo total da rota.

**O algoritmo de AGM (Kruskal) para obter um limite inferior para a solução do problema do caixeiro viajante.**
O algoritmo de Kruskal é um algoritmo de grafos que encontra uma árvore geradora mínima para um grafo conexo e ponderado, selecionando arestas em ordem crescente de peso e garantindo que não formem ciclos. Ele é eficiente e adequado para grafos densos ou esparsos.
  
**O Algoritmo de Christofides para o PCV**
O algoritmo de Christofides é uma heurística para o Problema do Caixeiro Viajante que oferece soluções aproximadas eficientes, combinando árvore mínima, emparelhamento perfeito mínimo e circuito Euleriano para encontrar rotas de viagem próximas ao ótimo.

## Instalação

**Algoritmo de força bruta**, você precisa ter as seguintes dependências instaladas:
Importações:
- import sys: Permite interagir com o sistema (ex: ler argumentos da linha de comando, encerrar o programa).
- import requests: Facilita o envio de requisições HTTP para interagir com a web de maneira simples e direta.
- from itertools import permutations Gera todas as permutações possíveis de um conjunto de elementos, útil para resolver problemas de combinação e permutação.

**Algoritmo de Dijkstra**
Este código Python implementa o algoritmo de Dijkstra para resolver o Problema do Caixeiro Viajante (TSP). Para executá-lo, instale as bibliotecas heapq, pandas, requests e io.

**Algoritmo de Kruskal**
- biblioteca requests: para fazer uma solicitação HTTP para obter os dados do URL.
- biblioteca StringIO: da biblioteca io para converter o texto da resposta em um objeto de arquivo que pode ser lido pelo pandas.
- biblioteca pandas: para ler os dados do arquivo de texto e convertê-lo em um DataFrame.
- biblioteca heapq: para implementar filas de prioridade (por exemplo, em algoritmos como Prim ou Dijkstra) se necessário.
  
**Algoritmo de Christofides** , você precisa ter as seguintes dependências instaladas:
- NetworkX: Biblioteca Python para criação, manipulação e estudo de redes complexas.
  Instalação via pip: ```pip install networkx```

- Requests: Biblioteca Python para fazer solicitações HTTP.
Instalação via pip: ``` pip install requests```

## Resultados
A seguir segue os custos minimos de cada base nos 4 algoritmos implementados no projeto.
| Bases                 | Força Bruta   | Dijkstra     |  Kruskal  | Christofides
| ----------------------| ------------- | -------------| ----------|----------|
| [1] - att48_d.txt     |               |              | 27670     | 54758    |
| [2] - dantzig42_d.txt |               |              | 591       | 1072     |
| [3] - five_d.txt      |     12        |              | 12        | 9        |
| [4] - fri26_d.txt     |               |              | 741       | 888      |
| [5] - gr17_d.txt      |               |              | 1421      | 1760     |
| [6] - p01_d.txt       |               |              | 260       | 190      |

## Contato do desenvolvedor
Nome e e-mail do(s) desenvolvedor(es):
- Douglas Alves: felipe.douglas.alves@hotmail.com
- Josué Junior: josue.junior@arapiraca.ufal.br
- Maria Izabel: maria.franca1@arapiraca.ufal.br
- Thalia Oliveira: thalia.oliveira@arapiraca.ufal.br

## Hardware sugerido
A configuração do sistema inclui um processador Ryzen 5 da série 7000, 8 GB de RAM e um SSD de 521 GB. O processador opera a 2.6 GHz e o sistema operacional foi Windowns10.
Software necessário: Todo o projeto está rodando no Colab.
