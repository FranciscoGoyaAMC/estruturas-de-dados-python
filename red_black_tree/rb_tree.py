from rb_node import RBNode


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True
        parent_node = None
        current = self.root
        while current != self.nil:
            parent_node = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return
        new_node.parent = parent_node
        if new_node.parent is None:
            self.root = new_node
        elif new_node.val < parent_node.val:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            parent = new_node.parent
            grandparent = parent.parent

            if grandparent is None:
                break

            if parent == grandparent.right:
                uncle = grandparent.left
                
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    if new_node == parent.left:
                        new_node = parent
                        self.rotate_right(new_node)
                        parent = new_node.parent
                    grandparent = parent.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)

            elif parent == grandparent.left:
                uncle = grandparent.right

                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    if new_node == parent.right:
                        new_node = parent
                        self.rotate_left(new_node)
                        parent = new_node.parent
                    grandparent = parent.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
                    
            self.root.red = False

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot
