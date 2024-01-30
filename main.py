import pandas as pd
import requests
from io import StringIO

# URL do arquivo de dados
url_bases = ["https://people.sc.fsu.edu/~jburkardt/datasets/tsp/att48_d.txt",
       "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/dantzig42_d.txt",
       "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/five_d.txt",
       "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/fri26_d.txt",
       "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/gr17_d.txt",
       "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/p01_d.txt"
       ]
try:
    print("""Escolha uma das bases de dados abaixo:
          [1] - att48_d.txt
          [2] - dantzig42_d.txt
          [3] - five_d.txt
          [4] - fri26_d.txt
          [5] - gr17_d.txt
          [6] - p01_d.txt
          """)
    escolha = int(input("Opção: "))
    url = url_bases[escolha - 1]

    # Obtendo os dados da URL
    response = requests.get(url)
    response.raise_for_status()

    data = StringIO(response.text)

    # Lendo os dados e criando um DataFrame
    df = pd.read_csv(data, delimiter="\s+", header=None)

    # Renomeando as colunas e índices
    df.columns = [f"V{i + 1}" for i in range(df.shape[1])]
    df.index = [f"V{i + 1}" for i in range(df.shape[0])]
    print(df)

    # Transformando Matriz de Distâncias em array
    lista_dataset = df.values.astype(int)
    print(lista_dataset)

except Exception as e:
    print(f"Ops... Ocorreu um erro. \nEscolha uma opçao dentre os valores acima")
