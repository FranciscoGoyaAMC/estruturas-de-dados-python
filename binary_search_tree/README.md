# Binary Search Tree (BST)

Este diretório contém uma implementação de Árvore Binária de Busca (Binary Search Tree) em Python, incluindo suporte para armazenar objetos customizados (como a classe `User`).

## Arquivos

- `bst_node.py`: Implementação da classe `BSTNode`, que representa um nó da árvore e fornece métodos para inserção, remoção, busca, travessias e cálculo de altura.
- `bst_node_doc.py`: Versão documentada da classe `BSTNode` com docstrings e comentários detalhados.
- `user.py`: Classe `User` para uso como valor nos nós da árvore, com métodos de comparação e geração de nomes.
- `user_doc.py`: Versão documentada da classe `User`.
- `test_bst.py`: Testes unitários para a árvore binária de busca utilizando a biblioteca `unittest`.
- `README.md`: Este arquivo de documentação.

## Funcionalidades

- Inserção de valores (inclusive objetos customizados) na árvore.
- Remoção de valores mantendo as propriedades da BST.
- Busca de valores (método `exists`).
- Recuperação do valor mínimo e máximo.
- Travessias em ordem, pré-ordem e pós-ordem.
- Cálculo da altura da árvore.

## Exemplo de Uso

```python
from bst_node import BSTNode
from user import User

bst = BSTNode()
users = [User(i) for i in range(5)]
for user in users:
    bst.insert(user)

print(bst.inorder([]))  # Travessia em ordem
print(bst.get_min())    # Menor valor
print(bst.get_max())    # Maior valor
print(bst.height())     # Altura da árvore
```

## Testes

Para rodar os testes unitários:

```bash
python test_bst.py
```

## Observações

- A árvore aceita qualquer objeto que implemente os métodos de comparação (`__lt__`, `__gt__`, `__eq__`).
- O código está documentado e pronto para uso didático ou como base para projetos mais avançados.
