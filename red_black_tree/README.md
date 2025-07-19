# Red-Black Tree em Python

Este diretório faz parte do repositório de estudos sobre estruturas de dados em Python, com foco em implementações do zero. Aqui você encontrará uma implementação completa de uma **Árvore Rubro-Negra (Red-Black Tree)**, uma estrutura de dados de árvore binária balanceada que garante eficiência em operações dinâmicas de inserção, remoção e busca.

---

## Sobre a Árvore Rubro-Negra

A Red-Black Tree é uma árvore binária de busca auto-balanceada que obedece a cinco regras fundamentais:

1. Cada nó é vermelho ou preto
2. A raiz é sempre preta
3. Todas as folhas (nil) são pretas
4. Um nó vermelho não pode ter filhos vermelhos
5. Todo caminho da raiz até as folhas nulas deve conter o mesmo número de nós pretos

Estas regras mantêm a altura da árvore aproximadamente logarítmica, garantindo **operações em O(log n)**.

---

## Arquivos e funcionalidades

### `rb_node.py` / `rb_node_doc.py`

Define a estrutura de um nó da Red-Black Tree:

* `val`: valor armazenado (pode ser uma chave primitiva ou objeto)
* `color`: vermelho (`'R'`) ou preto (`'B'`)
* Ponteiros para `left`, `right`, `parent`

### `rb_tree.py` / `rb_tree_doc.py`

Implementa a estrutura principal da Red-Black Tree com:

* Inserção balanceada com rotações e recolorimento
* Correção de propriedades após inserção (`fix_insert`)
* Impressão da árvore para visualização

### `user.py` / `user_doc.py`

Classe auxiliar usada para testes com objetos personalizados:

* `id`, `name`, `email`
* Implementa comparadores (`__lt__`, `__gt__`) para ordenação

### `test_rb_tree.py`

Script com testes de inserção usando dados simples e objetos `User`, incluindo:

* Impressão da árvore após inserções
* Verificação de propriedades visuais da estrutura balanceada

---

## Como executar os testes

```bash
cd red_black_tree
python test_rb_tree.py
```

---

## Exemplos de uso

Você pode inserir tanto valores primitivos quanto objetos com lógica de comparação definida:

```python
from rb_tree import RBTree
from user import User

tree = RBTree()
tree.insert(User(1, "Ana", "ana@email.com"))
tree.insert(User(2, "João", "joao@email.com"))
tree.insert(User(3, "Clara", "clara@email.com"))
```

---

## Objetivos desta implementação

* Compreender a complexidade de algoritmos de balanceamento
* Aplicar orientação a objetos na implementação de estruturas clássicas
* Servir como base para implementação de outras estruturas como **mapas ordenados**, **sets balanceados** e **árvores AVL**

---

## Autor

Francisco Goya
Estudante de Análise e Desenvolvimento de Sistemas
GitHub: [@FranciscoGoyaAMC](https://github.com/FranciscoGoyaAMC)

Sinta-se à vontade para explorar, sugerir melhorias ou contribuir! 🚀
