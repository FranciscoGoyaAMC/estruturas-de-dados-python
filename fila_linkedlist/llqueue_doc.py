class LLQueue:
    """
    Fila (Queue) baseada em lista encadeada (Linked List).

    Métodos:
        add_to_tail(node): Adiciona um nó ao final da fila.
        remove_from_head(): Remove e retorna o nó do início da fila.
        __iter__(): Itera sobre os nós da fila.
        __repr__(): Retorna uma representação em string da fila.
    """
    def __init__(self):
        """
        Inicializa uma fila vazia.
        """
        self.tail = None
        self.head = None

    def add_to_tail(self, node):
        """
        Adiciona um nó ao final da fila.

        Args:
            node (Node): O nó a ser adicionado.
        """
        if self.head is None:  # Verifica se a fila está vazia
            self.head = node  # Se estiver vazia, define a cabeça como o novo nó
            self.tail = node  # E também define a cauda como o novo nó
            return

        self.tail.set_next(node)  # Se a fila não estiver vazia, define o próximo nó da cauda atual para o novo nó
        self.tail = node  # Atualiza a cauda para o novo nó adicionado

    def remove_from_head(self):
        """
        Remove e retorna o nó do início da fila.

        Returns:
            Node | None: O nó removido ou None se a fila estiver vazia.
        """
        if self.head is None:  # Verifica se a fila está vazia
            return None
        temp_node = self.head  # Cria um nó temporário para armazenar o nó da cabeça
        self.head = self.head.next  # Atualiza a cabeça para o próximo nó na fila
        if self.head is None:  # Verifica se a nova cabeça é None
            self.tail = None  # Se for, também define a cauda como None, indicando que a fila está vazia. Isso evita referências circulares.
        temp_node.set_next(None)  # Limpa o próximo do nó temporário para evitar referências circulares.
        return temp_node  # Retorna o nó removido

    def __iter__(self):
        """
        Permite iteração sobre os nós da fila.

        Yields:
            Node: O próximo nó da fila.
        """
        node = self.head  # Setando a variável node para a cabeça da fila.
        while node is not None:  # Itera sobre os nós da fila, começando pela cabeça.
            yield node
            node = node.next  # Move para o próximo nó na fila.

    def __repr__(self):
        """
        Retorna uma representação em string da fila.

        Returns:
            str: String representando os valores dos nós na fila.
        """
        nodes = []  # Cria uma lista para armazenar os valores dos nós.
        for node in self:  # Itera sobre os nós e adiciona seus valores à lista.
            nodes.append(node.val)
        return " <- ".join(nodes)  # Retorna uma string com os valores dos nós separados por " <- ".
