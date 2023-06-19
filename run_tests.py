# //////////////////////////////////////////////////////////////////////////
# ///
# //////////////////////////////////////////////////////////////////////////

from canonical import * 
import sys
import random

# Caso de teste 1
g1 = [[0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]]

g2 = [[0, 1, 1, 0, 1],
            [1, 0, 1, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0]]


# Caso de teste 2
g3 = [[0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 1, 1],
            [0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0]]

g4 = [[0, 1, 1, 0, 1],
            [1, 0, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0]]


# Caso de teste 3
g5 = [[0, 1, 1],
            [1, 0, 0],
            [1, 0, 0]]

g6 = [[0, 1, 1],
            [1, 1, 0],
            [1, 0, 1]]



# //////////////////////////////////////////////////////////////////////////
# ///
# //////////////////////////////////////////////////////////////////////////


# Caso de teste 4: Grafos esparsos com 6 vértices
g7 = [[0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0]]

g8 = [[0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0]]

# Caso de teste 5: Grafos esparsos com 8 vértices
g9 = [[0, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0]]

g10 = [[0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0]]


# //////////////////////////////////////////////////////////////////////////
# ///
# //////////////////////////////////////////////////////////////////////////


# Caso de teste 6: Grafos densos com 5 vértices
g11 = [[0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0]]

g12 = [[0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0]]


# Caso de teste 7: Grafos densos com 6 vértices
g13 = [[0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 0]]

g14 = [[0, 1, 0, 1, 1, 0],
            [1, 0, 1, 1, 1, 1],
            [0, 1, 0, 1, 1, 0],
            [1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 0, 1],
            [0, 1, 0, 1, 1, 0]]


# //////////////////////////////////////////////////////////////////////////
# ///
# //////////////////////////////////////////////////////////////////////////


# Caso de teste 8: Grafos regulares com 4 vértices e grau 2
g15 = [[0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0]]

g16 = [[0, 1, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0]]


# Caso de teste 9: Grafos regulares com 5 vértices e grau 3
g17 = [[0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1],
            [1, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0]]

g18 = [[0, 0, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0]]



# //////////////////////////////////////////////////////////////////////////
# ///
# //////////////////////////////////////////////////////////////////////////


# Função para gerar um grafo aleatório com n vértices e densidade d
def generate_random_graph(n, density):
    g = [[0 for column in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < density:
                g[i][j] = 1
                g[j][i] = 1
    return g

# Caso de teste 10: Grafo aleatório com 6 vértices e densidade 0.5
g19 = generate_random_graph(6, 0.5)
g20 = generate_random_graph(6, 0.5)


# Caso de teste 11: Grafo aleatório com 8 vértices e densidade 0.3
g21 = generate_random_graph(8, 0.3)
g22 = generate_random_graph(8, 0.3)


test_cases = {
    1:  (g1,   g2),
    2:  (g3,   g4),
    3:  (g5,   g6),
    4:  (g7,   g8),
    5:  (g9,  g10),
    6:  (g11, g12),
    7:  (g13, g14),
    8:  (g15, g16),
    9:  (g17, g18),
    10: (g19, g20),
    11: (g21, g22),

}

test_cases2 = {
    'esparsos': [4, 5],
    'densos': [6, 7],
    'regulares': [8, 9],
    'aleatorios': [10,11]
}

def test(g1, g2, n):
    start_time = time.time()
    if isomorphic(g1, g2):
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
     
    elif tests == 'bench':
        n = 100
        while n < 20000:
            g1, g2 = generate_isomorphic_graphs(n)
            test(g1, g2, n)
            n = n * 2
    else:
        print("argumento invalido")


tests = sys.argv[1] if len(sys.argv) == 2 else ""
run_tests(tests)
