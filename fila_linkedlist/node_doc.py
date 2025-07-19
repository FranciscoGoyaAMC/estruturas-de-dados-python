class Node:
    """
    Classe Node representa um nó de uma lista encadeada.

    Atributos:
        val: Valor armazenado no nó.
        next: Referência para o próximo nó na lista (inicialmente None).

    Métodos:
        __init__(val): Inicializa o nó com um valor e o ponteiro next como None.
        set_next(node): Define o próximo nó da lista.
        __repr__(): Retorna uma representação em string do valor do nó.
    """

    def __init__(self, val):
        """
        Inicializa um novo nó.

        Args:
            val: O valor a ser armazenado no nó.
        """
        self.val = val          # Armazena o valor passado como argumento.
        self.next = None        # Inicialmente, o próximo nó é None.

    def set_next(self, node):
        """
        Define o próximo nó da lista.

        Args:
            node (Node): O próximo nó a ser referenciado.
        """
        self.next = node        # Atualiza o ponteiro next para o novo nó.

    def __repr__(self):
        """
        Retorna uma representação em string do valor do nó.

        Returns:
            str: O valor armazenado no nó.
        """
        return self.val         # Retorna o valor do nó como string.
    