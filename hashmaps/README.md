# HashMap

Este diretório contém uma implementação de tabela hash (HashMap) em Python, com tratamento de colisão por sondagem linear, redimensionamento dinâmico e suporte a remoção lógica (tombstone).

## Arquivos

- `hashmap.py`: Implementação principal da classe `HashMap`.
- `hashmap_doc.py`: Versão documentada da classe `HashMap` com docstrings e comentários detalhados.
- `user.py`: Classe `User` para uso como valor na tabela hash, com métodos de comparação e geração de nomes.
- `user_doc.py`: Versão documentada da classe `User`.
- `test_hashmap.py`: Testes automatizados para a tabela hash, cobrindo inserção, busca, remoção, colisão e redimensionamento.
- `README.md`: Este arquivo de documentação.

## Funcionalidades

- Inserção e atualização de pares chave-valor (`insert`).
- Busca de valores por chave (`get`).
- Remoção lógica de pares (`delete`) usando tombstone.
- Redimensionamento automático da tabela conforme a carga.
- Tratamento de colisão por sondagem linear.
- Suporte a qualquer tipo de valor, inclusive objetos customizados.

## Exemplo de Uso

```python
from hashmap import HashMap
from user import User

hashmap = HashMap(5)
user = User(42)
hashmap.insert("usuario42", user)
print(hashmap.get("usuario42"))  # Exibe o usuário inserido
hashmap.delete("usuario42")
# hashmap.get("usuario42")  # Levanta exceção: chave não encontrada
```

## Testes

Para rodar os testes automatizados:

```bash
python test_hashmap.py
```

## Observações

- O código está documentado e pode ser utilizado para fins didáticos ou como base para projetos maiores.
- A tabela hash aceita qualquer tipo de chave que seja string e qualquer tipo de valor.
- O tratamento de colisão e remoção lógica garante funcionamento correto mesmo em cenários de alta ocupação.
