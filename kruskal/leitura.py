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
        if escolha >=1 and escolha <=6:
            return self.url_bases[escolha - 1]
        return False

    def obter_dados(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return StringIO(response.text)

    def ler_dados(self, data):
        return pd.read_csv(data, delimiter="\s+", header=None)
