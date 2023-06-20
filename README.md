# Graph Isomorphism

Versão modificada do algoritmo de Ullmann.

## Como executar?

1. Clone o repositório.
2. Execute os testes.

```console
git clone https://github.com/igorvicentels/graph_isomorphism.git ullmann-modified
cd ullmann-modified
python run_tests.py <opcoes>
  - python run_tests.py "all" # Rodar todos testes
  - python run_tests.py "isomorfos" # Rodar testes só com grafos isomorfos
  - python run_tests.py "nao isomorfos" # Rodar testes só com grafos não isomorfos
  - python run_tests.py "gerados" # Rodar testes só com grafos isomorfos gerados

  - python run_tests.py "g[V]"
      # Rodar teste onde [V] é o numero de vertices dos grafos isomorfos
      # Por exemplo: "g27" vai rodar para 27 vértices
      # python run_tests.py "g27"
      # (Opções disponíveis: 27, 64, 125, 216, 343, 512, 729)

  - python run_tests.py "g[V]n"
      # Rodar teste onde [V] é o numero de vertices dos grafos não isomorfos
      # Por exemplo: "g27n" vai rodar para 27 vértices
      # python run_tests.py "g27n"
      # (Opções disponíveis: 27, 64, 125, 216, 343, 512, 729)
```
