class RBNode:
    """
    Classe RBNode representa um nó de uma Árvore Rubro-Negra (Red-Black Tree).

    Atributos:
        val: Valor armazenado no nó.
        red (bool): Indica se o nó é vermelho (True) ou preto (False).
        parent (RBNode | None): Referência para o nó pai.
        left (RBNode | None): Referência para o filho à esquerda.
        right (RBNode | None): Referência para o filho à direita.

    Métodos:
        __init__(val): Inicializa o nó com valor, cor preta e ponteiros nulos.
    """

    def __init__(self, val):
        """
        Inicializa um nó da árvore rubro-negra.

        Args:
            val: O valor a ser armazenado no nó.
        """
        self.red = False           # Por padrão, o nó é preto ao ser criado.
        self.parent = None         # Referência para o nó pai.
        self.val = val             # Valor armazenado no nó.
        self.left = None           # Filho à esquerda.
        self.right = None          # Filho à direita.
