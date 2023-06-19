import time


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


# Função para gerar o grafo completo com n nós
def generate_complete_graph(n):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            graph[i][j] = 1
            graph[j][i] = 1
    return graph


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time

        if exec_time < 1:
            time_converted = exec_time * 1000
            unit = 'ms'
        elif exec_time < 60:
            time_converted = exec_time
            unit = 's'
        else:
            time_converted = exec_time / 60
            unit = 'min'

        print(f'Tempo de execução: {time_converted:.2f}{unit}')

        return result

    return wrapper


@measure_execution_time
def main():
    graph1 = generate_complete_graph(100)
    graph2 = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
    ]

    if is_subgraph(graph1, graph2):
        print('O grafo 1 é um subgrafo do grafo 2.')
    else:
        print('O grafo 1 não é um subgrafo do grafo 2.')


if __name__ == '__main__':
    main()