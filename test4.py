def is_isomorphic(adj_matrix1, adj_matrix2):
    if len(adj_matrix1) != len(adj_matrix2):
        return False
    
    n = len(adj_matrix1)
    m = len(adj_matrix2)
    mapping = [-1] * n
    visited = [False] * m
    
    return backtrack(adj_matrix1, adj_matrix2, mapping, visited, 0)

def backtrack(adj_matrix1, adj_matrix2, mapping, visited, depth):
    if depth == len(adj_matrix1):
        return True
    
    u = depth
    for v in range(len(adj_matrix2)):
        if is_valid_mapping(adj_matrix1, adj_matrix2, mapping, u, v):
            mapping[u] = v
            visited[v] = True
            
            if backtrack(adj_matrix1, adj_matrix2, mapping, visited, depth + 1):
                return True
            
            mapping[u] = -1
            visited[v] = False
    
    return False

def is_valid_mapping(adj_matrix1, adj_matrix2, mapping, u, v):
    if adj_matrix1[u] != adj_matrix2[v]:
        return False
    
    for i in range(len(adj_matrix1)):
        if adj_matrix1[u][i] and not adj_matrix2[v][mapping[i]]:
            return False
    
    return True

import struct
import sys
from canonical import *


def read_graph(file, matrix):
    # Read the number of nodes
    nodes = struct.unpack('<H', file.read(2))[0]

    # Clean-up the matrix
    for i in range(nodes):
        matrix.append([0] * nodes)

    # For each node i ...
    for i in range(nodes):
        # Read the number of edges coming out of node i
        edges = struct.unpack('<H', file.read(2))[0]

        # For each edge out of node i...
        for j in range(edges):
            # Read the destination node of the edge
            target = struct.unpack('<H', file.read(2))[0]

            # Insert the edge in the adjacency matrix
            matrix[i][target] = 1

    return nodes

# Example usage
matrix1 = []
with open("iso_m3Dr2_s64.A01", "rb") as file:
    num_nodes = read_graph(file, matrix1)

g1 = matrix1

matrix2 = []
with open("iso_m3Dr2_s64.B01", "rb") as file:
    num_nodes = read_graph(file, matrix2)

g2 = matrix2

test_cases = {
    1:  (g1,   g2),
}

test_cases2 = {
    'esparsos': [4, 5],
    'densos': [6, 7],
    'regulares': [8, 9],
    'aleatorios': [10,11]
}

def test(g1, g2, n):
    start_time = time.time()
    if is_isomorphic(g1, g2):
        print(f"------------------------------------------------------\nCaso de Teste {n}: \nOs grafos são isomorfos")
    else:
        print(f"------------------------------------------------------\nCaso de Teste {n}: \nOs grafos não são isomorfos")

    end_time = time.time()

    if n in test_cases2['esparsos']:
        print(f"Os grafos são esparsos com {len(g1)} vértices")

    elif n in test_cases2['densos']:
        print(f"Os grafos são densos com {len(g1)} vértices")

    elif n in test_cases2['regulares']:
        print(f"Os grafos são regulares com {len(g1)} vértices")

    else:
        print(f"Os grafos têm {len(g1)} vértices")

    print("Tempo de execução em ms: ", (end_time - start_time)*1000)


def run_tests(tests=None):
    if tests == "":
        for i in test_cases:
            run_tests(i)

    elif tests in test_cases2:
        for i in test_cases2[tests]:
            run_tests(i)

    elif type(tests) == int:
        g1, g2 = test_cases[tests]
        test(g1, g2, tests)
    
    elif tests.isnumeric():
        g1, g2 = test_cases[int(tests)]
        test(g1, g2, tests)
     
    else:
        print("argumento invalido")


tests = sys.argv[1] if len(sys.argv) == 2 else ""
run_tests(tests)