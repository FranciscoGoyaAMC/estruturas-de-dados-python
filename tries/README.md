# Trie (Árvore de Prefixos)

Este diretório contém uma implementação de Trie (árvore de prefixos) em Python, estrutura eficiente para busca, inserção e análise de palavras e prefixos.

## Arquivos

- `tries.py`: Implementação principal da classe `Trie`.
- `tries_doc.py`: Versão documentada da classe `Trie` com docstrings e comentários detalhados.
- `test_tries.py`: Testes automatizados para a Trie, cobrindo inserção, busca, prefixos e buscas avançadas.
- `README.md`: Este arquivo de documentação.

## Funcionalidades

- Inserção de palavras (`add`).
- Verificação de existência de palavras (`exists`).
- Busca de todas as palavras com determinado prefixo (`words_with_prefix`).
- Busca de todas as substrings de um texto presentes no Trie (`find_matches`).
- Busca avançada considerando variações de caracteres (`advanced_find_matches`).
- Cálculo do maior prefixo comum entre todas as palavras (`longest_common_prefix`).

## Exemplo de Uso

```python
from tries import Trie

trie = Trie()
trie.add("casa")
trie.add("casamento")
trie.add("casaco")

print(trie.exists("casa"))  # True
print(trie.words_with_prefix("cas"))  # ['casa', 'casaco', 'casamento']
print(trie.longest_common_prefix())  # 'casa'
```

## Testes

Para rodar os testes automatizados:

```bash
python test_tries.py
```

## Observações

- A Trie é útil para autocomplete, correção ortográfica, busca de padrões e análise de textos.
- O código está documentado e pode ser utilizado para fins didáticos ou como base para projetos maiores.
