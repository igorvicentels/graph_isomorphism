def array_sum(A):
    return sum(A)


def num_rows(M):
    return len(M)


def num_cols(M):
    return len(M[0])


def array_2d_copy(A):
    return [row.copy() for row in A]


def check_square_matrix(A):
    s = len(A)
    for i in range(s):
        if len(A[i]) != s:
            return False
    return True


def map_P_to_G(M):
    def func(p):
        cols = num_cols(M)
        for c in range(cols):
            if M[p][c] == 1:
                return c
    return func


def is_iso(M, G, P):
    rows = num_rows(P)
    morph = map_P_to_G(M)
    for r1 in range(rows):
        for r2 in range(rows):
            if P[r1][r2] == 1:
                c1 = morph(r1)
                c2 = morph(r2)
                if G[c1][c2] != 1:
                    return False
    return True


def recurse(used_columns, cur_row, G, P, M, out, num, prune=False):
    cols = num_cols(M)
    if cur_row == num_rows(M):
        if is_iso(M, G, P):
            out.append(array_2d_copy(M))
    else:
        Mp = array_2d_copy(M)
        if prune:
            prune_options(Mp, P, G)
        for c in range(cols):
            if used_columns[c] == 0 and M[cur_row][c] == 1:
                for i in range(cols):
                    if i == c:
                        Mp[cur_row][i] = 1
                    else:
                        Mp[cur_row][i] = 0
                used_columns[c] = 1
                if num is None or len(out) < num:
                    recurse(used_columns, cur_row + 1, G, P, Mp, out, num)
                used_columns[c] = 0


def prune_options(M, P, G):
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] == 1:
                for x in range(len(P)):
                    if P[i][x] == 1:
                        has_neighbour_y = False
                        for y in range(len(G)):
                            if G[j][y] == 1:
                                has_neighbour_y = True
                                break
                        if not has_neighbour_y:
                            M[i][j] = 0


def degree_criteria(P, G, p, g):
    p_i_deg = array_sum(P[p])
    g_j_deg = array_sum(G[g])
    return p_i_deg <= g_j_deg


def init_morphism(G, P, criteria_fun=None):
    P_size = len(P)
    G_size = len(G)
    criteria_fun = criteria_fun or degree_criteria
    M = [[0] * G_size for _ in range(P_size)]
    for i in range(P_size):
        for j in range(G_size):
            if criteria_fun(P, G, i, j):
                M[i][j] = 1
    return M


def get_isomorphic_subgraphs(G, P, max_num=None, similarity_criteria=degree_criteria):
    G_size = len(G)
    P_size = len(P)
    if G_size < P_size:
        return []
    if max_num is not None and max_num <= 0:
        return []
    if not check_square_matrix(G) or not check_square_matrix(P):
        return None
    max_num = max_num or None
    M = init_morphism(G, P, similarity_criteria)
    results = []
    recurse([0] * G_size, 0, G, P, M, results, max_num, False)
    return results


# ///////////////////////////////////////////////////////////////////////////
# ///
# ///////////////////////////////////////////////////////////////////////////


G1 = [
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
]

P1 = [
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
]

G2 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
]

G = [[0,1,0], [0,0,1], [0,0,0]]

G3 = [[0,0,0], [0,0,0], [0,0,0]]
P3 = [[0,1,0], [0,0,1], [0,0,0]]

G4 = [[0,1,0], [0,0,1], [1,0,0]]

result = get_isomorphic_subgraphs(G1, P1)
if result:
    # print(result)
    print('isomorphic')
else:
    print('not isomorphic')

result = get_isomorphic_subgraphs(G2, P1)
if result:
    # print(result)
    print('isomorphic')
else:
    print('not isomorphic')

result = get_isomorphic_subgraphs(G, G)
if result:
    # print(result)
    print('isomorphic')
else:
    print('not isomorphic')

result = get_isomorphic_subgraphs(G3, P3)
if result:
    # print(result)
    print('isomorphic')
else:
    print('not isomorphic')

result = get_isomorphic_subgraphs(G4, G4)
if result:
    # print(result)
    print('isomorphic')
else:
    print('not isomorphic')