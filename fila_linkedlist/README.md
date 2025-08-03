# Fila com Lista Encadeada (Linked List Queue)

Este diretório implementa uma estrutura de dados de fila (queue) baseada em lista encadeada simples, utilizando as classes `Node` e `LLQueue`.

## Arquivos

- `node.py`: Implementação do nó da lista encadeada, com valor e ponteiro para o próximo nó.
- `node_doc.py`: Versão documentada da classe `Node`.
- `llqueue.py`: Implementação da fila baseada em lista encadeada, com métodos para inserção, remoção, iteração e representação.
- `llqueue_doc.py`: Versão documentada da classe `LLQueue`.
- `test_llqueue.py`: Testes automatizados para a fila, garantindo o funcionamento correto das operações básicas.
- `README.md`: Este arquivo de documentação.

## Funcionalidades

- Inserção de elementos no final da fila (`add_to_tail`).
- Remoção de elementos do início da fila (`remove_from_head`).
- Iteração sobre os elementos da fila.
- Representação em string da fila para fácil visualização.

## Exemplo de Uso

```python
from node import Node
from llqueue import LLQueue

fila = LLQueue()
fila.add_to_tail(Node("A"))
fila.add_to_tail(Node("B"))
fila.add_to_tail(Node("C"))

print(fila)  # Saída: A <- B <- C
print(fila.remove_from_head().val)  # Saída: A
print(fila)  # Saída: B <- C
```

## Testes

Para rodar os testes automatizados:

```bash
python test_llqueue.py
```

## Observações

- A fila utiliza uma lista encadeada simples, permitindo inserção e remoção eficientes.
- O código está documentado e pode ser utilizado para fins didáticos ou como base para projetos maiores.
