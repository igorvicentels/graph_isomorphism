# Pseudocódigo

# 1. Inicialize o vetor de caminho `path` com -1.
# 2. Chame a função `isomorph(path, 1)` para verificar a isomorfia.
# 3. Na função `isomorph(path, pos)`, faça o seguinte:
#    a. Se `pos` for igual ao número total de vértices no grafo, retorne True.
#    b. Para cada vértice `v` no grafo 2:
#       - Verifique se é seguro adicionar o vértice `v` ao caminho em posição `pos`.
#       - Se for seguro, atualize o caminho e chame recursivamente `isomorph` para o próximo vértice.
#       - Se a chamada recursiva retornar True, retorne True.
#       - Se não, desfaça a atualização do caminho.
#    c. Se nenhum vértice permitir um mapeamento válido, retorne False.
# 4. Se a função `isomorph` retornar True, os grafos são isomorfos. Caso contrário, não são isomorfos.

# Análise da complexidade

# A complexidade do algoritmo de Ullman depende do número de vértices e arestas nos grafos de entrada.
# Tempo de Execução:
# No pior caso, o algoritmo percorre todas as combinações possíveis de mapeamento entre os vértices dos dois grafos.
# O número de combinações possíveis é igual a n! (fatorial de n), onde n é o número de vértices do grafo.
# Portanto, a complexidade de tempo do algoritmo de Ullman é aproximadamente O(n!).
# Isso faz com que o algoritmo seja impraticável para grafos grandes, pois a fatorial cresce rapidamente.
# Espaço de memória:
# O algoritmo utiliza espaço de memória para armazenar o caminho atualmente percorrido e o mapeamento entre os vértices dos dois grafos.
# O espaço de memória necessário é proporcional ao número de vértices do grafo.
# Portanto, a complexidade de espaço do algoritmo de Ullman é O(n).
# É importante notar que o algoritmo de Ullman é um algoritmo de força bruta e, embora seja correto, sua complexidade exponencial o torna impraticável para grafos maiores. Para grafos maiores, são necessários algoritmos mais eficientes, como o algoritmo VF2 ou algoritmos baseados em técnicas avançadas, como a busca em largura (BFS) com backtracking.

import random
import time

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def is_safe(self, v, pos, path):
        # Verifica se é seguro adicionar o vértice v ao caminho em posição pos
        if self.graph[path[pos-1]][v] == 0:
            return False

        # Verifica se o vértice já foi visitado
        for vertex in path:
            if vertex == v:
                return False

        return True

    def isomorph(self, path, pos):
        # Caso base: se todos os vértices foram incluídos no caminho
        if pos == self.V:
            return True

        # Tenta adicionar vértices ao caminho
        for v in range(1, self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v

                if self.isomorph(path, pos+1):
                    return True

                path[pos] = -1
        return False

    def is_isomorphic(self, g2):
        print(self.graph)
        print()
        print(g2.graph)
        # Verifica se dois grafos são isomorfos
        if self.V != g2.V:
            return False

        print(1)
        # Inicializa o vetor de caminho com -1
        path = [-1] * self.V

        return self.isomorph(path, 1)

