# Pilha (Stack)

Este diretório contém uma implementação de pilha (Stack) em Python, utilizando uma lista nativa para armazenar os elementos.

## Arquivos

- `stack.py`: Implementação principal da classe `Stack`.
- `stack_doc.py`: Versão documentada da classe `Stack` com docstrings e comentários detalhados.
- `test_stack.py`: Testes automatizados para a pilha, cobrindo operações básicas.
- `README.md`: Este arquivo de documentação.

## Funcionalidades

- Inserção de elementos no topo da pilha (`push`).
- Remoção e retorno do elemento do topo (`pop`).
- Visualização do elemento do topo sem removê-lo (`peek`).
- Consulta do tamanho atual da pilha (`size`).

## Exemplo de Uso

```python
from stack import Stack

pilha = Stack()
pilha.push("A")
pilha.push("B")
pilha.push("C")

print(pilha.size())  # Saída: 3
print(pilha.peek())  # Saída: C
print(pilha.pop())   # Saída: C
print(pilha.pop())   # Saída: B
print(pilha.pop())   # Saída: A
print(pilha.pop())   # Saída: None
```

## Testes

Para rodar os testes automatizados:

```bash
python test_stack.py
```

## Observações

- A pilha utiliza uma lista nativa do Python, garantindo operações eficientes.
- O código está documentado e pode ser utilizado para fins didáticos ou como base para projetos maiores.
