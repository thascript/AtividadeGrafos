class Kruskal:
    @staticmethod
    def encontrar_AGM(matriz):
        agm = []  # Árvore geradora mínima
        subconjuntos = []

        n = len(matriz)

        # Função auxiliar para encontrar o subconjunto de um elemento 'i'
        def encontrar(pai, i):
            if pai[i] != i:
                pai[i] = encontrar(pai, pai[i])
            return pai[i]

        # Função auxiliar para realizar a união de dois subconjuntos x e y
        def unir(pai, classificacao, x, y):
            raiz_x = encontrar(pai, x)
            raiz_y = encontrar(pai, y)

            if classificacao[raiz_x] < classificacao[raiz_y]:
                pai[raiz_x] = raiz_y
            elif classificacao[raiz_x] > classificacao[raiz_y]:
                pai[raiz_y] = raiz_x
            else:
                pai[raiz_y] = raiz_x
                classificacao[raiz_x] += 1

        # Converter a matriz em uma lista de arestas
        arestas = []
        for i in range(n):
            for j in range(i + 1, n):
                if matriz[i][j] != 0:
                    arestas.append((i, j, matriz[i][j]))

        # Ordena as arestas em ordem crescente de peso
        arestas.sort(key=lambda x: x[2])

        # Inicializa os subconjuntos
        pai = [i for i in range(n)]
        classificacao = [0] * n

        i = 0  # Índice para percorrer as arestas
        while len(agm) < n - 1 and i < len(arestas):
            origem, destino, peso = arestas[i]

            raiz_origem = encontrar(pai, origem)
            raiz_destino = encontrar(pai, destino)

            # Se a adição da aresta não forma um ciclo, adiciona-a à árvore geradora mínima
            if raiz_origem != raiz_destino:
                agm.append((origem, destino, peso))
                unir(pai, classificacao, raiz_origem, raiz_destino)

            i += 1

        # Imprime as arestas da árvore geradora mínima
        custo_total = 0
        print("Arestas da Árvore Geradora Mínima.....:")
        for aresta in agm:
            origem, destino, peso = aresta
            print(f"{origem} -- {destino} (peso {peso})")
            custo_total += peso
        print("Custo Total: ", custo_total)
