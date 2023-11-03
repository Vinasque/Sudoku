import numpy as np
import networkx as nx

def vizinhos(num_quad, num_analise):
    sudoku = np.arange(1, num_quad**2 + 1).reshape(num_quad, num_quad)

    # Encontre a posição (linha e coluna) do número na matriz
    posicao = np.where(sudoku == num_analise)
    linha, coluna = posicao[0][0], posicao[1][0]

    linha_vizinhos = list(sudoku[linha, :])
    coluna_vizinhos = list(sudoku[:, coluna])

    # Encontre os números no mesmo bloco
    bloco_tamanho = int(sudoku.shape[0] ** 0.5)
    bloco_linha = linha // bloco_tamanho * bloco_tamanho
    bloco_coluna = coluna // bloco_tamanho * bloco_tamanho
    bloco_vizinhos = list(sudoku[bloco_linha:bloco_linha + bloco_tamanho, bloco_coluna:bloco_coluna + bloco_tamanho].flatten())

    vizinhos = set(linha_vizinhos + coluna_vizinhos + bloco_vizinhos) - {num_analise}

    return list(vizinhos)

def dicionario(n_quad):
    # Crie um grafo
    G = nx.Graph()

    # Adicione nós
    for n in range(1, n_quad ** 2 + 1):
        G.add_node(f"{n}")

    # Adicione arestas
    for n in range(1, n_quad ** 2 + 1):
        vizinhanca = vizinhos(n_quad, n)
        for num in vizinhanca:
            G.add_edge(f"{n}", f"{num}")

    # Cria o dicionário
    grafo_dicionario = dict()
    for vertice in G.nodes():
        vizinhos_vertice = list(G.neighbors(vertice))
        grafo_dicionario[vertice] = vizinhos_vertice

    return grafo_dicionario