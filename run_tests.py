import struct
import sys
import time
from ullmann import *

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

g = []
# 27 vertices
ga27 = []
for i in range(20):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_s27.A{n}", "rb") as file:
        read_graph(file, g)
        ga27.append(g)
        g = []

gb27 = []
for i in range(20):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_s27.B{n}", "rb") as file:
        read_graph(file, g)
        gb27.append(g)
        g = []

# 64 vertices
ga64 = []
for i in range(10):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_s64.A{n}", "rb") as file:
        read_graph(file, g)
        ga64.append(g)
        g = []

gb64 = []
for i in range(10):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_s64.B{n}", "rb") as file:
        read_graph(file, g)
        gb64.append(g)
        g = []

# 125 vertices
ga125 = []
for i in range(5):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_s125.A{n}", "rb") as file:
        read_graph(file, g)
        ga125.append(g)
        g = []

gb125 = []
for i in range(5):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_s125.B{n}", "rb") as file:
        read_graph(file, g)
        gb125.append(g)
        g = []

# 216 vertices
ga216 = []
for i in range(5):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_m216.A{n}", "rb") as file:
        read_graph(file, g)
        ga216.append(g)
        g = []

gb216 = []
for i in range(5):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_m216.B{n}", "rb") as file:
        read_graph(file, g)
        gb216.append(g)
        g = []


# 343 vertices
ga343 = []
for i in range(2):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_m343.A{n}", "rb") as file:
        read_graph(file, g)
        ga343.append(g)
        g = []

gb343 = []
for i in range(2):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_m343.B{n}", "rb") as file:
        read_graph(file, g)
        gb343.append(g)
        g = []

# 512 vertices
ga512 = []
for i in range(2):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_m512.A{n}", "rb") as file:
        read_graph(file, g)
        ga512.append(g)
        g = []

gb512 = []
for i in range(2):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_m512.B{n}", "rb") as file:
        read_graph(file, g)
        gb512.append(g)
        g = []

# 729 vertices
ga729 = []
for i in range(2):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_m729.A{n}", "rb") as file:
        read_graph(file, g)
        ga729.append(g)
        g = []

gb729 = []
for i in range(2):
    n = "%02d" % (i,)
    with open(f"data/iso_m3Dr2_m729.B{n}", "rb") as file:
        read_graph(file, g)
        gb729.append(g)
        g = []


def test(g1, g2, n):
    start_time = time.time()
    is_iso = is_isomorphic(g1, g2)
    if  is_iso:
        print(f"------------------------------------------------------\nCaso de Teste {n}: \nOs grafos são isomorfos")
    else:
        print(f"------------------------------------------------------\nCaso de Teste {n}: \nOs grafos não são isomorfos")

    end_time = time.time()

    print("Tempo de execução em ms: ", (end_time - start_time)*1000)

    return [end_time - start_time, True if is_iso else False]

test_cases = {
    "isomorfos": ["g27", "g64", "g125", "g216", "g343", "g512", "g729"],
    "nao isomorfos": ["g27n", "g64n", "g125n", "g216n", "g343n", "g512n", "g729n"]
}

info = {
    "g27": {},
    "g64": {},
    "g125": {},
    "g216": {},
    "g343": {},
    "g512": {},
    "g729": {},
    "g27n": {},
    "g64n": {},
    "g125n": {},
    "g216n": {},
    "g343n": {},
    "g512n": {},
    "g729n": {},
}

def run_tests(tests):
    if tests == "isomorfos":
        for i in test_cases["isomorfos"]:
            run_tests1(i)
    
    elif tests == "nao isomorfos":
        for i in test_cases["nao isomorfos"]:
            run_tests1(i)

    elif tests ==  "all":
        run_tests("isomorfos")
        run_tests("nao isomorfos")

def run_tests1(tests=None):
    if tests == "g27":
        for i in range(len(ga27)):
            info[tests][i] = test(ga27[i], gb27[i], i)

    elif tests == "g64":
        for i in range(len(ga64)):
            info[tests][i] = test(ga64[i], gb64[i], i)

    elif tests == "g125":
        for i in range(len(ga125)):
            info[tests][i] = test(ga125[i], gb125[i], i)

    elif tests == "g216":
        for i in range(len(ga216)):
            info[tests][i] = test(ga216[i], gb216[i], i)

    elif tests == "g343":
        for i in range(len(ga343)):
            info[tests][i] = test(ga343[i], gb343[i], i)

    elif tests == "g512":
        for i in range(len(ga512)):
            info[tests][i] = test(ga512[i], gb512[i], i)

    elif tests == "g729":
        for i in range(len(ga729)):
            info[tests][i] = test(ga729[i], gb729[i], i)

    elif tests == "g27n":
        for i in range(len(ga27) - 1):
            info[tests][i] = test(ga27[i], gb27[i+1], i)

    elif tests == "g64n":
        for i in range(len(ga64) - 1):
            info[tests][i] = test(ga64[i], gb64[i+1], i)

    elif tests == "g125n":
        for i in range(len(ga125) - 1):
            info[tests][i] = test(ga125[i], gb125[i+1], i)

    elif tests == "g216n":
        for i in range(len(ga216) - 1):
            info[tests][i] = test(ga216[i], gb216[i+1], i)

    elif tests == "g343n":
        for i in range(len(ga343) - 1):
            info[tests][i] = test(ga343[i], gb343[i+1], i)

    elif tests == "g512n":
        for i in range(len(ga512) - 1):
            info[tests][i] = test(ga512[i], gb512[i+1], i)

    elif tests == "g729n":
        for i in range(len(ga729) - 1):
            info[tests][i] = test(ga729[i], gb729[i+1], i)
     
    else:
        print("argumento invalido")


    sum_time = 0
    for item in info[tests]:
        sum_time += info[tests][item][0]

    n_iso = 0
    for item in info[tests]:
        n_iso += info[tests][item][1]

    temp_m = (sum_time / (len(info[tests]))) * 1000
    info[tests]["n_tests"] = len(info[tests])
    info[tests]["time"] = temp_m
    info[tests]["n_iso"] = n_iso


def write_to_file(tests):
    n_tests = info[tests]['n_tests']
    n_acertos = info[tests]["n_iso"] if tests[-1] != "n" else  n_tests - info[tests]["n_iso"]

    s = "-------------------------------------------\n"
    if tests[-1] == "n":
        s += f"Grupo de testes: {tests} [NÂO ISOMORFOS]\n\n"
    else:
        s += f"Grupo de testes: {tests}\n\n"

    s += f"Número de testes: {n_tests}\n"
    s += f"Número de acertos: {n_acertos}\n"
    s += f"Tempo médio: {info[tests]['time']} ms\n"
    
    f.write(s)

tests = sys.argv[1] if len(sys.argv) == 2 else ""

run_tests(tests)

with open("filename", "w") as f:
    if tests == "isomorfos":
        for test in test_cases["isomorfos"]:
            write_to_file(test)
    
    elif tests == "nao isomorfos":
        for test in test_cases["nao isomorfos"]:
            write_to_file(test)

    elif tests == "all":
        for test in test_cases["isomorfos"]:
            write_to_file(test)
        for test in test_cases["nao isomorfos"]:
            write_to_file(test)
    else:
        write_to_file(test)
