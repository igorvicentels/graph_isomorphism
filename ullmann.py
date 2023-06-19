import copy

# Teste se grafo1 é isomorfico a algum subgrafo do grafo2
def is_isomorphic(graph1, graph2):
    # Cria lista para armazenar possiveis vertices equivalentes. 
    # pos_assignments[3] = [1,4,5] significa que os vertices 1, 4 e 5 do graph2 podem ser equivalentes ao vertice 3 do graph1
    pos_assignments = [[] for _ in graph1]

    # Verifica quais nós do graph1 tem grau menor que os nós do graph2 e guarda o resultado em pos_assignments 
    for i in range(len(graph1)):
        for j in range(len(graph2)):
            if sum(graph1[i]) <= sum(graph2[j]):
                pos_assignments[i].append(j)

    # Refine
    while True:
        new_assignments = refine(graph1, graph2, pos_assignments)
        if pos_assignments == new_assignments:
            break
        pos_assignments = new_assignments

    mappings = []
    return find_isomorphism(graph1, graph2, pos_assignments, mappings)

# Verifica se os vizinhos de i no grafo1 podem ser mapeados para os vizinhos de j no grafo2
def is_candidate(i, j, graph1, graph2, pos_assignments):
    count = 0
    # Checa se os vizinhos de i são todos candidatos de algum vertice de grafo2
    for idx1, v1 in enumerate(graph1[i]):
        # Caso o v1 seja adjacente a i no grafo1
        if v1 == 1: 
            count = 0
            # Checa se esse vertice é candidato de algum vertice do grafo2 vizinho a j
            for idx2, v2 in enumerate(graph2[j]): 
                if v2 == 1:
                    if idx2 in pos_assignments[idx1]:
                        count += 1
            if count == 0:
                return False
    return True


def refine(graph1, graph2, pos_assignments):
    new_assignments = copy.deepcopy(pos_assignments)
    for i in range(len(graph1)):
        for j in new_assignments[i]:
            if not is_candidate(i, j, graph1, graph2, new_assignments):
                new_assignments[i].remove(j)
    return new_assignments

def find_isomorphism(graph1, graph2, pos_assignments, mappings):
    a = len(mappings)
    new_assignments = copy.deepcopy(pos_assignments)

    if len(graph1) == a:
        return mappings

    for i in new_assignments[a]:
        # Checa se algum vertice do grafo 1 ja foi mapeado para o vertice i do grafo 2 
        if i in list(map(lambda x: x[1], mappings)):
            continue

        mappings.append((a,i))
        # Assign nó a do grafo 1 para o nó i do grafo 2
        new_assignments[a] = [i] 
        # Tira o no i de todos os outros possiveis nos de a
        new_assignments = list(map(lambda x: x if x == new_assignments[a] else list(filter(lambda y: y != i, x)), new_assignments)) 
        # aplica o procedimento de refine
        # new_assignments = refine(graph1, graph2, new_assignments) 

        # Checa se algum nó de a ficou sem possibilidades
        has_empty_assignments = len(list(filter(lambda x: x == [], new_assignments))) > 0 
       
        if has_empty_assignments:
            mappings.pop(-1)
            new_assignments = copy.deepcopy(pos_assignments)
            continue

        result = find_isomorphism(graph1, graph2, new_assignments, mappings)
        if result is not None:
            return result

    return None

