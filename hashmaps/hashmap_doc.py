class HashMap:
    """
    Classe HashMap implementa uma tabela hash com tratamento de colisão por sondagem linear e redimensionamento dinâmico.

    Atributos:
        TOMBSTONE: Objeto especial para marcar posições deletadas.
        hashmap (list): Lista que armazena os pares (chave, valor) ou TOMBSTONE/None.

    Métodos:
        insert(key, value): Insere ou atualiza um par chave-valor.
        get(key): Retorna o valor associado à chave.
        delete(key): Remove um par chave-valor.
        resize(): Redimensiona a tabela hash quando necessário.
        current_load(): Retorna a carga atual da tabela.
        key_to_index(key): Converte uma chave em índice.
        __repr__(): Retorna uma representação em string da tabela hash.
    """

    TOMBSTONE = object()  # Objeto especial para marcar posições deletadas

    def __init__(self, size):
        """
        Inicializa a tabela hash com o tamanho especificado.

        Args:
            size (int): Tamanho inicial da tabela hash.
        """
        self.hashmap = [None for i in range(size)]  # Cria a lista de tamanho 'size' preenchida com None

    def insert(self, key, value):
        """
        Insere ou atualiza um par chave-valor na tabela hash.

        Args:
            key (str): Chave a ser inserida.
            value: Valor associado à chave.
        """
        self.resize()  # Redimensiona a tabela se necessário
        index = self.key_to_index(key)  # Calcula o índice inicial para a chave
        # Procura uma posição livre ou com a mesma chave (atualização)
        while self.hashmap[index] and self.hashmap[index] != self.TOMBSTONE and self.hashmap[index][0] != key:
            index = (index + 1) % len(self.hashmap)  # Sondagem linear
        self.hashmap[index] = (key, value)  # Insere ou atualiza o par (chave, valor)

    def get(self, key):
        """
        Retorna o valor associado à chave, se existir.

        Args:
            key (str): Chave a ser buscada.

        Returns:
            Valor associado à chave.

        Raises:
            Exception: Se a chave não for encontrada.
        """
        index = self.key_to_index(key)  # Calcula o índice inicial
        checked = 0  # Contador para evitar loop infinito
        # Procura a chave na tabela, considerando colisões
        while self.hashmap[index] and checked < len(self.hashmap):
            if self.hashmap[index] != self.TOMBSTONE and self.hashmap[index][0] == key:
                return self.hashmap[index][1]  # Retorna o valor se encontrar a chave
            index = (index + 1) % len(self.hashmap)  # Sondagem linear
            checked += 1
        raise Exception("sorry, key not found")  # Chave não encontrada

    def delete(self, key):
        """
        Remove um par chave-valor da tabela hash.

        Args:
            key (str): Chave a ser removida.

        Raises:
            Exception: Se a chave não for encontrada.
        """
        index = self.key_to_index(key)  # Calcula o índice inicial
        checked = 0  # Contador para evitar loop infinito
        # Procura a chave na tabela
        while self.hashmap[index] and checked < len(self.hashmap):
            if self.hashmap[index] != self.TOMBSTONE and self.hashmap[index][0] == key:
                self.hashmap[index] = self.TOMBSTONE  # Marca como deletado
                return
            index = (index + 1) % len(self.hashmap)  # Sondagem linear
            checked += 1
        raise Exception("sorry, key not found")  # Chave não encontrada

    def resize(self):
        """
        Redimensiona a tabela hash se a carga for maior que 5%.
        """
        if len(self.hashmap) == 0:
            self.hashmap = [None]  # Garante que a tabela nunca fique vazia
        if self.current_load() < 0.05:
            return  # Não redimensiona se a carga for baixa
        old_hashmap = self.hashmap  # Guarda a tabela antiga
        new_hashmap = HashMap((len(old_hashmap)*10))  # Cria nova tabela maior
        for item in old_hashmap:
            if item is not None:
                key, value = item
                new_hashmap.insert(key, value)  # Reinsere os itens na nova tabela
        self.hashmap = new_hashmap.hashmap  # Atualiza a referência para a nova tabela

    def current_load(self):
        """
        Retorna a carga atual da tabela hash (proporção de posições ocupadas).

        Returns:
            float: Carga da tabela hash.
        """
        if len(self.hashmap) == 0:
            return 1  # Considera carga máxima se a tabela estiver vazia
        return sum(1 for item in self.hashmap if item is not None) / len(self.hashmap)  # Proporção ocupada

    def key_to_index(self, key) -> int:
        """
        Converte uma chave em um índice da tabela hash.

        Args:
            key (str): Chave a ser convertida.

        Returns:
            int: Índice correspondente na tabela hash.
        """
        total = 0  # Inicializa a soma dos códigos dos caracteres
        for c in key:  # Para cada caractere na chave
            total += ord(c)  # Soma o valor Unicode do caractere
        return total % len(self.hashmap)  # Retorna o índice calculado

    def __repr__(self):
        """
        Retorna uma representação em string da tabela hash.

        Returns:
            str: Representação da tabela hash, mostrando índices e valores.
        """
        final = ""  # String que irá acumular a representação
        for i, v in enumerate(self.hashmap):  # Percorre todos os índices e valores
            if v is not None:
                final += f" - {i}: {str(v)}\n"  # Mostra o índice e o par (chave, valor)
            else:
                final += f" - {i}: None\n"  # Mostra None se a posição estiver vazia
        return final
