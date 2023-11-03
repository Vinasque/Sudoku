def coloracao_por_vertice(grafo):
    cores = {} 

    for vertice in grafo:
        vizinhos = grafo[vertice]
        print(vizinhos) 

        cores_vizinhos = set(cores.get(v, None) for v in vizinhos)

        # Encontre a menor cor não usada pelos vizinhos
        cor = 0
        while cor in cores_vizinhos:
            cor += 1

        cores[vertice] = cor

    return cores

def dicionario_cores(cores):
    grupos = {}
    
    for vertice, cor in cores.items():
        if cor not in grupos:
            grupos[cor] = []
        grupos[cor].append(vertice)
    
    return grupos