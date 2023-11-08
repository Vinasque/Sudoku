from funcoes import vizinhos
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def grafo(n_quad, nome):
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

    # Daqui para baixo é só estética

    # Organize os vértices pelo valor do vértice em ordem crescente no sentido horário
    vertices_crescentes = sorted(G.nodes(), key=lambda x: int(x), reverse=True)
    angulos = np.linspace(0, 2 * np.pi, len(G.nodes()), endpoint=False)
    posicao = {vertice: (np.cos(angulos[i]), np.sin(angulos[i])) for i, vertice in enumerate(vertices_crescentes)}

    # Defina as cores dos nós
    vertices_cores = ['white'] * len(G.nodes())
    vertices_cores_borda = ['black'] * len(G.nodes())

    # O formato do grafo personalizado
    plt.figure(figsize=(280, 280))
    nx.draw(G, posicao, with_labels = True, node_color = vertices_cores, edge_color='black', node_size=500, font_weight='bold')
    nx.draw_networkx_edges(G, posicao, edgelist = G.edges(), edge_color='black', width=2)  # Desenhe as arestas novamente para que fiquem acima dos nós
    nx.draw_networkx_nodes(G, posicao, node_color = 'white', node_size = 500, node_shape = 'o', edgecolors = vertices_cores_borda, linewidths = 2)

    plt.axis('off')
    plt.savefig(nome)
    plt.show()