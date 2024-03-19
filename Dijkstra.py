import heapq
import pandas as pd
import requests
from io import StringIO

class LeitorDados:
    def __init__(self):
        self.url_bases = [
            "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/att48_d.txt",
            "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/dantzig42_d.txt",
            "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/five_d.txt",
            "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/fri26_d.txt",
            "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/gr17_d.txt",
            "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/p01_d.txt"
        ]

    def escolher_base(self):
        print("""Escolha uma das bases de dados abaixo:
              [1] - att48_d.txt
              [2] - dantzig42_d.txt
              [3] - five_d.txt
              [4] - fri26_d.txt
              [5] - gr17_d.txt
              [6] - p01_d.txt
              """)
        escolha = int(input("Opção: "))
        if escolha >= 1 and escolha <= 6:
            return self.url_bases[escolha - 1]
        return False

    def obter_dados(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return StringIO(response.text)

    def ler_dados(self, data):
        # Definir um separador personalizado para lidar com espaços em branco
        return pd.read_csv(data, delim_whitespace=True, header=None)



def encontrar_menor_caminho(grafo, s):
    n = len(grafo)
    visitado = [False] * n
    caminho = []
    custo_total = 0

    atual = s
    visitado[atual] = True
    caminho.append(atual)

    # Escolha do próximo vértice com o menor custo que não foi visitado
    for _ in range(n-1):
        proximo = None
        menor_custo = float('inf')
        for v in range(n):
            if not visitado[v] and 0 < grafo[atual][v] < menor_custo:
                proximo = v
                menor_custo = grafo[atual][v]
        if proximo is not None:
            visitado[proximo] = True
            caminho.append(proximo)
            custo_total += menor_custo
            atual = proximo

    # Retornar ao início
    custo_total += grafo[atual][s]
    caminho.append(s)

    return caminho, custo_total



leitor = LeitorDados()

url = leitor.escolher_base()
if url:
    # adc um clear aqui...
    base = leitor.obter_dados(url)

    df = leitor.ler_dados(base)
    matriz = df.values.astype(int)
else:
    print("Opção inválida. \n")
    url = leitor.escolher_base()

# Exemplo de uso


caminho, custo = encontrar_menor_caminho(matriz, 0)
print("Caminho:", caminho)
print("Custo total:", custo)