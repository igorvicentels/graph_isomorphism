import struct
def is_subgraph(graph1, graph2):
    n1, n2 = len(graph1), len(graph2)

    # Verificar se o número de vértices no grafo1 é maior do que no grafo2
    if n1 > n2:
        return False

    # Função auxiliar para verificar a correspondência dos vértices dos grafos
    def is_vertex_match(v1, v2):
        for i in range(n1):
            if graph1[v1][i] == 1 and graph2[v2][i] != 1:
                return False
        return True

    # Função auxiliar para verificar a correspondência das arestas dos grafos
    def is_edge_match(v1, v2):
        for i in range(n1):
            for j in range(n1):
                if graph1[v1][i] == 1 and graph1[v1][j] == 1:
                    if graph2[v2][i] != 1 or graph2[v2][j] != 1:
                        return False
        return True

    # Função principal do algoritmo de Ullman
    def ullman(v1, v2, mapping):
        if v1 == n1:
            return True

        for v in range(n2):
            if is_vertex_match(v1, v) and is_edge_match(v1, v):
                mapping[v1] = v

                if ullman(v1 + 1, v2, mapping):
                    return True

                mapping[v1] = None

        return False

    mapping = [None] * n1
    return ullman(0, 0, mapping)



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
matrix = []
with open("iso_m3Dr2_s27.A01", "rb") as file:
    num_nodes = read_graph(file, matrix)
    print("Number of nodes:", num_nodes)
    print("Adjacency matrix:")
    for i in range(num_nodes):
        for j in range(num_nodes):
            print(matrix[i][j], end=" ")
        print()
g1 = matrix

matrix = []
with open("iso_m3Dr2_s27.B01", "rb") as file:
    num_nodes = read_graph(file, matrix)

g2 = matrix

if is_subgraph(g1, g2):
    print("O grafo 1 é um subgrafo do grafo 2.")
else:
    print("O grafo 1 não é um subgrafo do grafo 2.")