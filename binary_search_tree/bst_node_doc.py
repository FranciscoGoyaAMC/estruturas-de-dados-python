class BSTNode:
    """
    Classe BSTNode representa um nó de uma Árvore Binária de Busca (Binary Search Tree).

    Atributos:
        val: Valor armazenado no nó.
        left: Referência para o filho à esquerda (BSTNode ou None).
        right: Referência para o filho à direita (BSTNode ou None).

    Métodos:
        insert(val): Insere um valor na árvore seguindo as regras da BST.
        get_min(): Retorna o menor valor da árvore/subárvore.
        get_max(): Retorna o maior valor da árvore/subárvore.
        delete(val): Remove um valor da árvore e reorganiza os nós.
        preorder(visited): Retorna uma lista dos valores em pré-ordem.
        postorder(visited): Retorna uma lista dos valores em pós-ordem.
        inorder(visited): Retorna uma lista dos valores em ordem.
        exists(val): Verifica se um valor existe na árvore.
        height(): Retorna a altura da árvore/subárvore.
    """

    def __init__(self, val=None):
        """
        Inicializa um nó da BST.

        Args:
            val: O valor a ser armazenado no nó.
        """
        self.left = None  # Inicializa o filho da esquerda como None
        self.right = None  # Inicializa o filho da direita como None
        self.val = val  # Armazena o valor no nó

    def insert(self, val):
        """
        Insere um valor na árvore binária de busca.

        Args:
            val: O valor a ser inserido.
        """
        if not self.val:
            self.val = val  # Se o nó estiver vazio, define o valor diretamente
            return
        if val == self.val:
            return  # Não permite valores duplicados
        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)  # Cria novo nó à esquerda se estiver vazio
            else:
                self.left.insert(val)  # Insere recursivamente à esquerda
        if val > self.val:
            if self.right is None:
                self.right = BSTNode(val)  # Cria novo nó à direita se estiver vazio
            else:
                self.right.insert(val)  # Insere recursivamente à direita

    def get_min(self):
        """
        Retorna o menor valor da árvore/subárvore.

        Returns:
            O menor valor encontrado.
        """
        node = self  # Começa no nó atual
        while node.left:
            node = node.left  # Vai o mais à esquerda possível
        return node.val  # Retorna o valor mínimo

    def get_max(self):
        """
        Retorna o maior valor da árvore/subárvore.

        Returns:
            O maior valor encontrado.
        """
        node = self  # Começa no nó atual
        while node.right:
            node = node.right  # Vai o mais à direita possível
        return node.val  # Retorna o valor máximo

    def delete(self, val):
        """
        Remove um valor da árvore e reorganiza os nós.

        Args:
            val: O valor a ser removido.

        Returns:
            BSTNode | None: Raiz da árvore após remoção.
        """
        if self.val is None:
            return None  # Caso base: árvore vazia
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)  # Repassa a chamada à esquerda
            return self
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)  # Repassa a chamada à direita
            return self
        else:
            if self.right is None:
                return self.left  # Substitui nó pelo filho esquerdo
            if self.left is None:
                return self.right  # Substitui nó pelo filho direito
            # Caso com dois filhos: substitui pelo menor da subárvore direita
            successor = self.right.get_min()
            self.val = successor  # Substitui valor
            self.right = self.right.delete(successor)  # Remove o sucessor da subárvore
            return self

    def preorder(self, visited):
        """
        Retorna uma lista dos valores em pré-ordem.

        Args:
            visited (list): Lista de valores visitados.

        Returns:
            list: Valores em pré-ordem.
        """
        visited.append(self.val)  # Adiciona o valor a lista de visited
        if self.left:
            self.left.preorder(visited)  # Visita a subárvore esquerda
        if self.right:
            self.right.preorder(visited)  # Visita a subárvore direita
        return visited

    def postorder(self, visited):
        """
        Retorna uma lista dos valores em pós-ordem.

        Args:
            visited (list): Lista de valores visitados.

        Returns:
            list: Valores em pós-ordem.
        """
        if self.left:
            self.left.postorder(visited)  # Visita a subárvore esquerda
        if self.right:
            self.right.postorder(visited)  # Visita a subárvore direita
        visited.append(self.val)  # Adiciona o valor a lista de visited
        return visited

    def inorder(self, visited):
        """
        Retorna uma lista dos valores em ordem.

        Args:
            visited (list): Lista de valores visitados.

        Returns:
            list: Valores em ordem.
        """
        if self.left:
            self.left.inorder(visited)  # Visita a subárvore esquerda
        visited.append(self.val)  # Adiciona o valor a lista de visited
        if self.right:
            self.right.inorder(visited)  # Visita a subárvore direita
        return visited

    def exists(self, val):
        """
        Verifica se um valor existe na árvore.

        Args:
            val: O valor a ser buscado.

        Returns:
            bool: True se o valor existe, False caso contrário.
        """
        if self.val == val:
            return True  # Valor encontrado
        if val < self.val and self.left:
            return self.left.exists(val)  # Busca recursiva à esquerda
        if val > self.val and self.right:
            return self.right.exists(val)  # Busca recursiva à direita
        return False  # Valor não encontrado

    def height(self):
        """
        Retorna a altura da árvore/subárvore.

        Returns:
            int: Altura da árvore.
        """
        if self.val is None:
            return 0  # Se a árvore for vazia retorna 0
        # Usa max() para verificar qual altura é o maior caminho até uma folha, somado a 1
        return max(self.left.height() if self.left else 0, self.right.height() if self.right else 0) + 1
