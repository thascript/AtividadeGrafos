import networkx as nx
import requests
import time


# Função para carregar os dados de um arquivo TSP
def carregar_dados_tsp(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        dados = [list(map(float, linha.strip().split())) for linha in linhas[6:] if linha.strip()]
    return dados



# Função para calcular a matriz de distância a partir dos dados carregados

# Função para calcular a matriz de distância a partir dos dados carregados
def calcular_matriz_distancia(dados):
    num_nos = len(dados)
    matriz_distancia = [[0] * num_nos for _ in range(num_nos)]
    for i in range(num_nos):
        for j in range(i + 1, num_nos):
            dx = dados[i][1] - dados[j][1]
            dy = dados[i][2] - dados[j][2]
            matriz_distancia[i][j] = matriz_distancia[j][i] = (dx ** 2 + dy ** 2) ** 0.5
    return matriz_distancia




# Função para criar um grafo completo a partir da matriz de distância
def criar_grafo_completo(matriz_distancia):
    num_nos = len(matriz_distancia)
    G = nx.Graph()
    for i in range(num_nos):
        for j in range(i + 1, num_nos):
            G.add_edge(i, j, weight=matriz_distancia[i][j])
    return G


# Função para calcular a árvore geradora mínima
def arvore_geradora_minima(grafo):
    return nx.minimum_spanning_tree(grafo)


# Função para encontrar nós com grau ímpar na árvore geradora mínima
def encontrar_nos_grau_impar(grafo):
    odd_degree_nodes = []
    for node in grafo.nodes():
        if grafo.degree(node) % 2 != 0:
            odd_degree_nodes.append(node)
    return odd_degree_nodes


# Função para calcular o emparelhamento perfeito de peso mínimo
def emparelhamento_perfeito_peso_minimo(grafo, nos):
    max_weight_matching = nx.max_weight_matching(grafo, weight='weight')
    min_weight_matching = nx.Graph()
    for u, v in max_weight_matching:
        min_weight_matching.add_edge(u, v, weight=grafo[u][v]['weight'])
    return min_weight_matching


# Função para combinar dois grafos
def combinar_grafos(grafo1, grafo2):
    combined_graph = nx.Graph()
    if grafo1.edges() or grafo2.edges():
        combined_graph.add_edges_from(grafo1.edges(data=True))
        combined_graph.add_edges_from(grafo2.edges(data=True))
    else:
        combined_graph.add_node(0)  # Adiciona pelo menos um nó
    return combined_graph


# Função para encontrar o circuito euleriano
def circuito_euleriano(grafo):
    circuit = []
    stack = [list(grafo.nodes())[0]]

    while stack:
        current_node = stack[-1]
        neighbors = list(grafo.neighbors(current_node))

        if neighbors:
            next_node = neighbors[0]
            grafo.remove_edge(current_node, next_node)
            stack.append(next_node)
        else:
            circuit.append(stack.pop())

    return circuit[::-1]



# Função para calcular o custo total do passeio
def calcular_custo_passeio(passeio, matriz_distancia):
    total_cost = 0
    for i in range(len(passeio) - 1):
        total_cost += matriz_distancia[passeio[i]][passeio[i + 1]]
    return total_cost


# Função principal para executar o algoritmo de Christofides para um conjunto de dados
def executar_algoritmo_christofides():
    url_bases = [
        "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/att48_d.txt",
        "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/dantzig42_d.txt",
        "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/five_d.txt",
        "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/fri26_d.txt",
        "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/gr17_d.txt",
        "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/p01_d.txt"
    ]
    for url in url_bases:
        start_time = time.time()

        # Carregar dados do conjunto de dados
        response = requests.get(url)
        dados = [list(map(float, linha.split())) for linha in response.text.split("\n")[2:] if linha.strip()]
       

        # Calcular matriz de distância
        matriz_distancia = calcular_matriz_distancia(dados)

        # Criar grafo completo
        grafo_completo = criar_grafo_completo(matriz_distancia)

        # Calcular árvore geradora mínima
        arvore_min_spanning = arvore_geradora_minima(grafo_completo)

        # Encontrar nós de grau ímpar na árvore geradora mínima
        nos_grau_impar = encontrar_nos_grau_impar(arvore_min_spanning)

        # Calcular emparelhamento perfeito de peso mínimo
        emparelhamento_min_peso = emparelhamento_perfeito_peso_minimo(grafo_completo, nos_grau_impar)

        # Combinar árvore geradora mínima e emparelhamento perfeito
        grafo_aumentado = combinar_grafos(arvore_min_spanning, emparelhamento_min_peso)

        # Encontrar circuito euleriano
        circuito_euleriano_arestas = circuito_euleriano(grafo_aumentado)

        # Remover nós repetidos
        tour = list(dict.fromkeys(circuito_euleriano_arestas))

        # Calcular o custo total do passeio
        custo_total = calcular_custo_passeio(tour, matriz_distancia)

        end_time = time.time()
        tempo_execucao = end_time - start_time

        # Imprimir resultados
        print("\n### Base de dados:", url.split("/")[-1])
        print("Minimização da distância:", tour)
        print("Custo mínimo:", custo_total)
        print("Tempo de execução:", tempo_execucao)


# Executar o algoritmo
executar_algoritmo_christofides()
