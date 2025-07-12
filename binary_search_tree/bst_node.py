class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if val == self.val:
            return
        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        if val > self.val:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)


    def get_min(self):
        node = self
        while node.left:
            node = node.left
        return node.val
            

    def get_max(self):
        node = self
        while node.right:
            node = node.right
        return node.val
    

    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        else:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            successor = self.right.get_min()
            self.val = successor
            self.right = self.right.delete(successor)
            return self
        

    def preorder(self, visited):
        visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)
        return visited
    

    def postorder(self, visited):
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        visited.append(self.val)
        return visited
    

    def inorder(self, visited):
        if self.left:
            self.left.inorder(visited)
        visited.append(self.val)
        if self.right:
            self.right.inorder(visited)
        return visited


    def exists(self, val):
        if self.val == val:
            return True
        if val < self.val and self.left:
            return self.left.exists(val)
        if val > self.val and self.right:
            return self.right.exists(val)
        return False
    

    def height(self):
        if self.val is None:
            return 0
        return max(self.left.height() if self.left else 0, self.right.height() if self.right else 0) + 1
    