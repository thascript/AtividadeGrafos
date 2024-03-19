from leitura import LeitorDados
from kruskal import Kruskal

class Aplicacao:
    def __init__(self):
        self.leitor = LeitorDados()
        self.kruskal = Kruskal()

    def executar(self):
        url = self.leitor.escolher_base()
        if url:
            base = self.leitor.obter_dados(url)
            df = self.leitor.ler_dados(base)
            matriz = df.values.astype(int)

            self.kruskal.encontrar_AGM(matriz)
        else:
            print("Ops, opção inválida.\n")
            self.executar()

if __name__ == "__main__":
    app = Aplicacao()
    app.executar()
