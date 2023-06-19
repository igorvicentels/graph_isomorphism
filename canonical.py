import time


def canonical_labeling(graph):
  degrees = [0] * len(graph)
  for i in range(len(graph)):
    for j in range(len(graph)):
      if graph[i][j] == 1:
        degrees[i] += 1
  sorted_vertices = sorted(range(len(graph)), key=lambda i: degrees[i], reverse=True)
  canonical_labeling = []
  for i in sorted_vertices:
    canonical_labeling.append(i)
  return canonical_labeling


def isomorphic(graph1, graph2):
  canonical_labeling1 = canonical_labeling(graph1)
  canonical_labeling2 = canonical_labeling(graph2)
  return canonical_labeling1 == canonical_labeling2


def generate_isomorphic_graphs(vertex):
  # Cria uma matriz de adjacência vazia para o primeiro grafo
  graph1 = [[0] * vertex for _ in range(vertex)]

  # Preenche a matriz de adjacência para o primeiro grafo
  for i in range(vertex):
    j = (i + 1) % vertex
    graph1[i][j] = 1
    graph1[j][i] = 1

  # Cria uma matriz de adjacência vazia para o segundo grafo
  graph2 = [[0] * vertex for _ in range(vertex)]

  # Preenche a matriz de adjacência para o segundo grafo
  for i in range(vertex):
    j = (i + 2) % vertex
    graph2[i][j] = 1
    graph2[j][i] = 1

  return [graph1, graph2]


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
  # graph1 = [
  #   [0, 1, 0, 0, 1],
  #   [1, 0, 1, 0, 0],
  #   [0, 1, 0, 1, 0],
  #   [0, 0, 1, 0, 1],
  #   [1, 0, 0, 1, 0],
  # ]
  # graph2 = [
  #   [0, 0, 0, 1, 1],
  #   [0, 0, 1, 1, 0],
  #   [0, 1, 0, 0, 1],
  #   [1, 1, 0, 0, 0],
  #   [1, 0, 1, 0, 0],
  # ]
  # graph1 = [
  #   [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
  #   [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
  #   [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
  #   [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
  #   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
  #   [0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
  #   [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
  #   [0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
  #   [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
  #   [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
  # ]
  # graph2 = [
  #   [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
  #   [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
  #   [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
  #   [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
  #   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
  #   [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
  #   [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
  #   [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
  #   [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
  #   [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
  # ]
  # graph1 = [
  #   [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  #   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  #   [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  #   [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
  #   [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
  #   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
  #   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
  #   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
  #   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
  #   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
  #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
  #   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
  #   [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
  #   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
  # ]
  # graph2 = [
  #   [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  #   [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #   [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  #   [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #   [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
  #   [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  #   [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
  #   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
  #   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
  #   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
  #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
  #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
  #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  #   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
  # ]

  graph1, graph2 = generate_isomorphic_graphs(25600)
  # print(graph1)
  # print(graph2)

  print(isomorphic(graph1, graph2))


if __name__ == "__main__":
  main()