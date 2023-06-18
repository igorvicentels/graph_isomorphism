def printm(matrix):
    for i in range(len(matrix)):
        for j in matrix[i]:
            print(f" {j} ", end="")
        print('\n')

import copy

# Teste se grafo1 é subgrafo do grafo2
def algo(graph1, graph2):
    ullmann = [[0] * len(graph2) for _ in range(len(graph1))]

    # Verifica quais nós do graph1 tem grau menor que os nós do graph2 e guarda o resultado na matrix ullmannn 
    for i in range(len(graph1)):
        for j in range(len(graph2)):
            ullmann[i][j] = 1 if sum(graph1[i]) <= sum(graph2[j]) else 0

    # Refine
    while True:
        newUllmann = refine(graph1, graph2, ullmann)
        if ullmann == newUllmann:
            break
        ullmann = newUllmann

    path = []
    searched = []

    print(find_isomorphism(graph1, graph2, ullmann, path, searched))

# Verifica se os vizinhos de i no grafo1 podem ser mapeados para os vizinhos de j no grafo2
def is_candidate(i, j, graph1, graph2, ullmann):
    count = 0
    # Checa se os vizinhos de i são todos candidatos de algum vertice de grafo2
    for idx1, v1 in enumerate(graph1[i]):
        if v1 == 1: # Caso o v1 seja adjacente a i no grafo1
            count = 0
            # Checa se esse vertice é candidato de algum vertice do grafo2 vizinho a j
            for idx2, v2 in enumerate(graph2[j]): 
                if v2 == 1:
                    if ullmann[idx1][idx2] == 1:
                        count += 1
                        continue
            if count == 0:
                return False
    return True


def refine(graph1, graph2, ullmann):
    new_ullmann = copy.deepcopy(ullmann)
    for i in range(len(graph1)):
        for j in range(len(graph2)):
            if new_ullmann[i][j] == 1:
                if not is_candidate(i, j, graph1, graph2, ullmann):
                    new_ullmann[i][j] = 0
    return new_ullmann

def make_column_zero(lst, i, row_index):
    result = [row[:] for row in lst]
    for idx, row in enumerate(result):
        if idx != row_index:
            row[i] = 0
    return result

def find_isomorphism(graph1, graph2, ullmann, path, searched):
    a = len(path)

    if len(graph1) == a:
        return path

    for i in range(len(ullmann[a])):
        if ullmann[a][i] and (a, i) not in searched:

            path.append((a, i))
            searched.append((a, i))
            new_ullmann = make_column_zero(ullmann, i, a)

            result = find_isomorphism(graph1, graph2, new_ullmann, path, searched)
            if result is not None:
                return result
        
            # Rollback
            new_ullmann = copy.deepcopy(ullmann) 
            path.pop(-1)
            searched.pop(-1)
    return None

graph1 = [
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
]


graph2 = [
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0]
]

printm(make_column_zero(graph2, 3, 4))

algo(graph1, graph2)


# print(searched)
    



