# Graphs (Grafos)

Este diretório contém uma implementação de grafos não direcionados em Python, utilizando dicionários de adjacências para representar conexões entre vértices.

## Arquivos

- `graph.py`: Implementação principal da classe `Graph`.
- `graph_doc.py`: Versão documentada da classe `Graph` com docstrings e comentários detalhados.
- `test_graph.py`: Testes automatizados para o grafo, cobrindo inserção de arestas, buscas e propriedades do grafo.
- `README.md`: Este arquivo de documentação.

## Funcionalidades

- Adição de arestas entre vértices (`add_edge`).
- Verificação de existência de aresta (`edge_exists`).
- Busca em largura (BFS) e busca em profundidade (DFS).
- Listagem de vértices desconectados (`unconnected_vertices`).
- Visualização das conexões do grafo (`__repr__`).

## Exemplo de Uso

```python
from graph import Graph

g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")

print(g.breadth_first_search("A"))  # Saída: ['A', 'B', 'C', 'D']
print(g.depth_first_search("A"))    # Saída: ['A', 'B', 'D', 'C']
print(g.edge_exists("A", "B"))     # True
print(g.unconnected_vertices())      # Lista de vértices sem conexões
print(g)                             # Visualização do grafo
```

## Testes

Para rodar os testes automatizados:

```bash
python test_graph.py
```

## Observações

- O grafo é não direcionado e armazena as conexões em ambos os sentidos.
- O código está documentado e pode ser utilizado para fins didáticos ou como base para projetos maiores.
