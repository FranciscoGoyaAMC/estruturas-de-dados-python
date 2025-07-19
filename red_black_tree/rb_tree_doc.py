from rb_node import RBNode


class RBTree:
    """
    Classe RBTree representa uma Árvore Rubro-Negra (Red-Black Tree).

    Atributos:
        nil (RBNode): Nó sentinela representando folhas nulas.
        root (RBNode): Raiz da árvore.

    Métodos:
        insert(val): Insere um valor na árvore mantendo as propriedades rubro-negras.
        fix_insert(new_node): Corrige violações das propriedades após inserção.
        rotate_left(pivot_parent): Rotaciona um nó para a esquerda.
        rotate_right(pivot_parent): Rotaciona um nó para a direita.
    """

    def __init__(self):
        """
        Inicializa a árvore rubro-negra com nó sentinela nil.
        """
        self.nil = RBNode(None)       # Cria o nó sentinela nil (folhas nulas)
        self.nil.red = False          # Nó nil é sempre preto
        self.nil.left = None          # Nil não tem filhos
        self.nil.right = None
        self.root = self.nil          # A raiz inicial aponta para o nil

    def insert(self, val):
        """
        Insere um novo valor na árvore rubro-negra.

        Args:
            val: O valor a ser inserido.
        """
        new_node = RBNode(val)        # Cria um novo nó com o valor fornecido
        new_node.left = self.nil      # Define filhos como nil
        new_node.right = self.nil
        new_node.red = True           # Novos nós são vermelhos inicialmente

        parent_node = None
        current = self.root

        # Busca pela posição correta de inserção
        while current != self.nil:
            parent_node = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return  # Valor duplicado não é inserido

        new_node.parent = parent_node  # Define o pai do novo nó

        # Caso seja o primeiro nó da árvore, vira a raiz
        if new_node.parent is None:
            self.root = new_node
        elif new_node.val < parent_node.val:
            parent_node.left = new_node  # Insere como filho à esquerda
        else:
            parent_node.right = new_node  # Insere como filho à direita

        self.fix_insert(new_node)  # Corrige possíveis violações após inserção

    def fix_insert(self, new_node):
        """
        Corrige violações das propriedades rubro-negras após inserção.

        Args:
            new_node (RBNode): O nó recém-inserido.
        """
        # Enquanto o pai for vermelho (violação da regra de dois vermelhos consecutivos)
        while new_node != self.root and new_node.parent.red:
            parent = new_node.parent
            grandparent = parent.parent

            if grandparent is None:
                break

            # Caso o pai esteja na direita do avô
            if parent == grandparent.right:
                uncle = grandparent.left  # Tio está à esquerda

                if uncle.red:
                    # Caso 1: tio é vermelho → recoloração
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    # Caso 2 e 3: tio é preto
                    if new_node == parent.left:
                        # Caso 2: rotação para direita no pai
                        new_node = parent
                        self.rotate_right(new_node)
                        parent = new_node.parent
                    # Caso 3: rotação para esquerda no avô
                    grandparent = parent.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)

            # Caso o pai esteja na esquerda do avô
            elif parent == grandparent.left:
                uncle = grandparent.right  # Tio está à direita

                if uncle.red:
                    # Caso 1: tio é vermelho → recoloração
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    # Caso 2 e 3: tio é preto
                    if new_node == parent.right:
                        # Caso 2: rotação para esquerda no pai
                        new_node = parent
                        self.rotate_left(new_node)
                        parent = new_node.parent
                    # Caso 3: rotação para direita no avô
                    grandparent = parent.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)

            # Após qualquer modificação, a raiz deve continuar preta
            self.root.red = False

    def rotate_left(self, pivot_parent):
        """
        Realiza rotação à esquerda em torno de um nó.

        Args:
            pivot_parent (RBNode): O nó em torno do qual a rotação será feita.
        """
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return

        pivot = pivot_parent.right               # O nó à direita se tornará o novo pai
        pivot_parent.right = pivot.left          # Substitui o filho direito pelo filho esquerdo do pivot
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent     # Atualiza o pai do filho movido
        pivot.parent = pivot_parent.parent       # O novo pai aponta para o avô

        if pivot_parent.parent is None:
            self.root = pivot                    # Atualiza a raiz se necessário
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot     # Liga o pivot ao lado esquerdo do avô
        else:
            pivot_parent.parent.right = pivot    # Ou ao lado direito do avô

        pivot.left = pivot_parent                # O nó original se torna filho à esquerda
        pivot_parent.parent = pivot              # Atualiza o pai

    def rotate_right(self, pivot_parent):
        """
        Realiza rotação à direita em torno de um nó.

        Args:
            pivot_parent (RBNode): O nó em torno do qual a rotação será feita.
        """
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return

        pivot = pivot_parent.left                # O nó à esquerda se tornará o novo pai
        pivot_parent.left = pivot.right          # Substitui o filho esquerdo pelo filho direito do pivot
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent    # Atualiza o pai do filho movido
        pivot.parent = pivot_parent.parent       # O novo pai aponta para o avô

        if pivot_parent.parent is None:
            self.root = pivot                    # Atualiza a raiz se necessário
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot    # Liga o pivot ao lado direito do avô
        else:
            pivot_parent.parent.left = pivot     # Ou ao lado esquerdo do avô

        pivot.right = pivot_parent               # O nó original se torna filho à direita
        pivot_parent.parent = pivot              # Atualiza o pai
