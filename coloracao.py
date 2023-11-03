def coloracao_por_vertice(grafo):
    cores = {}

    # Loop sobre todos os vértices do grafo
    for vertice in grafo:
        cores_disponiveis = set(range(1, int(len(grafo) ** 0.5) + 1))  # Conjunto de cores disponíveis
        for vizinho in grafo[vertice]:
            if vizinho in cores:
                cores_disponiveis.discard(cores[vizinho])  # Remova cores usadas pelos vizinhos
        if cores_disponiveis:
            cor = min(cores_disponiveis)  # Atribua a menor cor disponível
            cores[vertice] = cor

    return cores