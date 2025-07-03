class Stack:
    """
    Classe Stack representa uma pilha (stack) utilizando uma lista nativa do Python.

    Métodos:
        push(item): Insere um item no topo da pilha.
        pop(): Remove e retorna o item do topo da pilha.
        peek(): Retorna o item do topo sem removê-lo.
        size(): Retorna o tamanho atual da pilha.
    """

    def __init__(self):
        """
        Inicializa uma pilha vazia.
        """
        self.items = [] # Inicializa a lista que armazenará os itens da pilha.

    def push(self, item):
        """
        Insere um item no topo da pilha.

        Args:
            item: O item a ser inserido na pilha.
        """
        self.items.append(item) # Adiciona o item ao final da lista, que representa o topo da pilha.

    def size(self):
        """
        Retorna o tamanho atual da pilha.

        Returns:
            int: O número de itens na pilha.
        """
        return len(self.items) # Retorna o comprimento da lista que contém os itens da pilha.

    def peek(self):
        """
        Retorna o item do topo da pilha sem removê-lo.

        Returns:
            O item do topo da pilha, ou None se a pilha estiver vazia.
        """
        if self.items:  # Verifica se a pilha não está vazia.
            return self.items[-1] # Retorna o último item da lista, que é o topo da pilha.
        return None # Se a pilha estiver vazia, retorna None.

    def pop(self):
        """
        Remove e retorna o item do topo da pilha.

        Returns:
            O item removido do topo da pilha, ou None se a pilha estiver vazia.
        """
        if self.items:  # Verifica se a pilha não está vazia.
            top_item = self.items[-1]  # Armazena o item do topo da pilha.
            del self.items[-1]  # Remove o item do topo da pilha.
            return top_item  # Retorna o item removido.
        return None  # Se a pilha estiver vazia, retorna None.
