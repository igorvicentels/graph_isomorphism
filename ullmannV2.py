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
    print(mappings)
    new_assignments = copy.deepcopy(pos_assignments)

    if len(graph1) == a:
        return mappings

    for i in new_assignments[a]:
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

    # if mappings:
    #     mappings.pop(-1)
    #     new_assignments = copy.deepcopy(pos_assignments)
        # todo: talvez precise adicionar rollback do new_assignments
    return None

graph1 = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], 
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
]


graph2 = [
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], 
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], 
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
]



# printm(make_column_zero(graph2, 3, 4))

# print(is_isomorphic(graph2, graph1))
# x = [(0, 33), (0, 44), (2, 0), (2, 2), (2, 4), (2, 7), (6, 8), (7, 2), (8, 37), (9, 24), (10, 22), (11, 15), (12, 8), (13, 12), (11, 50), (15, 15), (16, 56), (17, 0), (18, 7), (19, 63), (20, 21), (21, 11), (22, 53), (23, 20), (24, 10), (25, 47), (26, 12), (27, 16), (28, 49), (29, 1), (30, 39), (31, 55), (20, 43), (33, 55), (34, 38), (35, 9), (36, 40), (37, 42), (38, 27), (17, 30), (40, 29), (41, 23), (42, 5), (42, 63), (6, 26), (45, 40), (46, 56), (47, 0), (47, 2), (47, 4), (47, 8), (47, 11), (47, 13), (47, 15), (47, 17), (47, 19), (47, 21), (47, 23), (47, 25), (47, 28), (60, 21), (61, 16), (62, 3), (63, 58)]
# y = list(map(lambda a: a[1], x))
# y.sort()
# print(y)

# mappings = [1,2,3,4,5,6]
# mappings.pop(-1)
# print(mappings)
    
# a = [(0, 0), (1, 1), (2, 2), (3, 4), (4, 9), (5, 5), (6, 6), (7, 3), (8, 7), (8, 8), (10, 10), (11, 18), (12, 12), (13, 13), (14, 14), (15, 20), (16, 15), (17, 16), (18, 19), (19, 21), (20, 11), (21, 24), (22, 17), (23, 25), (24, 22), (24, 23), (26, 26)]
# a1 = list(map(lambda x: x[1], a))
# a1.sort()
# print(a1)


