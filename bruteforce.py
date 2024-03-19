import sys
import requests
from itertools import permutations

# Função para baixar e carregar os dados de uma URL
def carregar_dados(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Levanta um erro para erros HTTP (4xx, 5xx)
        linhas = resposta.text.strip().split('\n')
        # Os dados são considerados como uma matriz de adjacência, onde grafo[i][j] é a distância da cidade i para a cidade j
        grafo = [list(map(float, linha.split())) for linha in linhas]
        return grafo
    except requests.RequestException as e:
        print(f"Erro ao baixar dados de {url}: {e}")
        sys.exit(1)  # Sai do programa em caso de erro ao carregar os dados

# Solução do problema do Caixeiro Viajante com força bruta
def forca_bruta(grafo, origem):
    # Atenção: Esta função tem complexidade de tempo fatorial e pode ser muito lenta para grafos com muitos vértices.
    vertices = [i for i in range(len(grafo)) if i != origem]
    caminho_minimo = sys.maxsize
    proxima_permutacao = permutations(vertices)
    for permutacao in proxima_permutacao:
        peso_atual = sum(grafo[k][j] for k, j in zip([origem] + list(permutacao), list(permutacao) + [origem]))
        caminho_minimo = min(caminho_minimo, peso_atual)
    return caminho_minimo

# Função para exibir o menu e obter a entrada do usuário
def exibir_menu(urls):
    print("Escolha os conjuntos de dados para executar:")
    for idx, url in enumerate(urls):
        print(f"{idx+1}. {url}")
    print("0. Sair")
    escolha = input("Digite o número do conjunto de dados (1-6) ou 0 para sair: ")
    return escolha

urls_bases = [
    "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/att48_d.txt",
    "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/dantzig42_d.txt",
    # Adicione mais URLs conforme necessário
]

# Loop principal
while True:
    escolha = exibir_menu(urls_bases)

    if escolha == '0':
        print("Encerrando...")
        break

    try:
        escolha = int(escolha)
        if escolha < 1 or escolha > len(urls_bases):
            raise ValueError("Escolha inválida.")
        
        url = urls_bases[escolha - 1]
        print(f"Conjunto de dados {escolha}: {url}")

        grafo = carregar_dados(url)
        print("Dados carregados com sucesso.")
        
        # Força bruta para encontrar o caminho mínimo
        cidade_origem = 0  # Pode ser ajustado conforme necessário
        caminho_minimo_forca_bruta = forca_bruta(grafo, cidade_origem)
        print(f"Comprimento mínimo do caminho com força bruta: {caminho_minimo_forca_bruta}")
        
    except ValueError as ve:
        print(f"Escolha inválida: {ve}")
    except Exception as e:
        print(f"Erro ao processar conjunto de dados: {e}")
    
    print()