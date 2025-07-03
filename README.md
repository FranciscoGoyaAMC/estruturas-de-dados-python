# Estruturas de Dados em Python

Este repositório contém implementações de estruturas de dados clássicas utilizando Python, com foco em aprendizado, eficiência e compreensão dos fundamentos da Ciência da Computação. Cada estrutura foi desenvolvida do zero, sem uso de bibliotecas externas, buscando compreender profundamente seu funcionamento interno.

Para cada estrutura, o repositório inclui:

* Uma versão **clean**, enxuta, ideal para uso direto em outros projetos
* Uma versão **documentada**, com explicações passo a passo e docstrings educativas

## Estruturas implementadas

### 📁 pilha\_array/

Implementação de uma **Pilha (Stack)** utilizando uma lista nativa do Python.

* Operações:

  * `push`: insere um item no topo da pilha
  * `pop`: remove o item do topo
  * `peek`: consulta o topo sem remover
  * `size`: retorna o tamanho da pilha

* Arquivos:

  * `stack.py`: versão clean da pilha
  * `stack_doc.py`: versão documentada da pilha
  * `test_stack.py`: testes com asserts para validar o comportamento

### 📁 fila\_linkedlist/

Implementação de uma **Fila (Queue)** baseada em **lista encadeada (linked list)** com operações eficientes em O(1).

* Estrutura:

  * `Node`: representa um nó da lista
  * `LLQueue`: estrutura da fila

* Operações:

  * `add_to_tail`: insere um nó ao final da fila
  * `remove_from_head`: remove o nó do início da fila

* Arquivos:

  * `node.py`: versão clean da classe Node
  * `node_doc.py`: versão documentada da classe Node
  * `llqueue.py`: versão clean da fila
  * `llqueue_doc.py`: versão documentada da fila
  * `test_llqueue.py`: testes para a fila encadeada

---

## Como executar os testes

Acesse cada pasta e execute o arquivo de teste correspondente:

```bash
cd pilha_array
python test_stack.py

cd ../fila_linkedlist
python test_llqueue.py
```

---

## Objetivos deste repositório

* Consolidar o conhecimento prático em estruturas de dados
* Desenvolver implementações eficientes e didáticas
* Servir como base para futuras estruturas mais complexas:

  * ✅ Árvores Binárias
  * ✅ Hashmaps
  * ✅ Grafos
  * ✅ Árvores Red-Black

---

## Autor

Francisco Goya  
Estudante de Análise e Desenvolvimento de Sistemas  
GitHub: [@FranciscoGoyaAMC](https://github.com/FranciscoGoyaAMC)  
LinkedIn: [Francisco Goya](https://www.linkedin.com/in/francisco-goya-de-almeida-martins-costa-0a8ab9327/)

Sinta-se à vontade para explorar, sugerir melhorias ou contribuir! 🚀
