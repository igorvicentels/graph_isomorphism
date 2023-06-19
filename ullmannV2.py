def printm(matrix):
    for i in range(len(matrix)):
        for j in matrix[i]:
            print(f" {j} ", end="")
        print('\n')

import copy

# Teste se grafo1 é subgrafo do grafo2
def is_isomorphic(graph1, graph2):
    # Cria lista para armazenar possiveis vertices equivalentes. 
    # pos_assigments[3] = [1,4,5] significa que os vertices 1, 4 e 5 do graph2 podem ser equivalentes ao vertice 3 do graph1
    pos_assigments = [[] for _ in graph1]

    # Verifica quais nós do graph1 tem grau menor que os nós do graph2 e guarda o resultado em pos_assigments 
    for i in range(len(graph1)):
        for j in range(len(graph2)):
            if sum(graph1[i]) <= sum(graph2[j]):
                pos_assigments[i].append(j)

    # Refine
    while True:
        new_assigments = refine(graph1, graph2, pos_assigments)
        if pos_assigments == new_assigments:
            break
        pos_assigments = new_assigments

    path = []
    searched = []

    return find_isomorphism(graph1, graph2, pos_assigments, path, searched)

# Verifica se os vizinhos de i no grafo1 podem ser mapeados para os vizinhos de j no grafo2
def is_candidate(i, j, graph1, graph2, pos_assigments):
    count = 0
    # Checa se os vizinhos de i são todos candidatos de algum vertice de grafo2
    for idx1, v1 in enumerate(graph1[i]):
        # Caso o v1 seja adjacente a i no grafo1
        if v1 == 1: 
            count = 0
            # Checa se esse vertice é candidato de algum vertice do grafo2 vizinho a j
            for idx2, v2 in enumerate(graph2[j]): 
                if v2 == 1:
                    if idx2 in pos_assigments[idx1]:
                        count += 1
            if count == 0:
                return False
    return True


def refine(graph1, graph2, pos_assigments):
    new_assigments = copy.deepcopy(pos_assigments)
    for i in range(len(graph1)):
        for j in new_assigments[i]:
            if not is_candidate(i, j, graph1, graph2, new_assigments):
                new_assigments[i].remove(j)
    return new_assigments

def find_isomorphism(graph1, graph2, pos_assigments, path, searched):
    a = len(path)
    # print(path)
    new_assigments = copy.deepcopy(pos_assigments)

    if len(graph1) == a:
        return path

    for i in new_assigments[a]:
        path.append((a,i))
        searched.append((a,i))
        # Assign nó a do grafo 1 para o nó i do grafo 2
        new_assigments[a] = [i] 
        # Tira o no i de todos os outros possiveis nos de a
        new_assigments = list(map(lambda x: x if x == new_assigments[a] else list(filter(lambda y: y != i, x)), new_assigments)) 
        # aplica o procedimento de refine
        new_assigments = refine(graph1, graph2, new_assigments) 

        # Checa se algum nó de a ficou sem possibilidades
        has_empty_assigments = len(list(filter(lambda x: x == [], new_assigments))) > 0 
       
        if has_empty_assigments:
            path.pop(-1)
            searched.pop(-1)
            new_assigments = copy.deepcopy(pos_assigments)
            continue

        result = find_isomorphism(graph1, graph2, new_assigments, path, searched)
        if result is not None:
            return result

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

# algo(graph1, graph2)
# x = [(0, 33), (0, 44), (2, 0), (2, 2), (2, 4), (2, 7), (6, 8), (7, 2), (8, 37), (9, 24), (10, 22), (11, 15), (12, 8), (13, 12), (11, 50), (15, 15), (16, 56), (17, 0), (18, 7), (19, 63), (20, 21), (21, 11), (22, 53), (23, 20), (24, 10), (25, 47), (26, 12), (27, 16), (28, 49), (29, 1), (30, 39), (31, 55), (20, 43), (33, 55), (34, 38), (35, 9), (36, 40), (37, 42), (38, 27), (17, 30), (40, 29), (41, 23), (42, 5), (42, 63), (6, 26), (45, 40), (46, 56), (47, 0), (47, 2), (47, 4), (47, 8), (47, 11), (47, 13), (47, 15), (47, 17), (47, 19), (47, 21), (47, 23), (47, 25), (47, 28), (60, 21), (61, 16), (62, 3), (63, 58)]
# y = list(map(lambda a: a[1], x))
# y.sort()
# print(y)

# path = [1,2,3,4,5,6]
# path.pop(-1)
# print(path)
    



