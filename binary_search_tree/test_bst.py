import unittest
from bst_node import BSTNode
from user import User, get_users


class TestBSTNode(unittest.TestCase):
    def setUp(self):
        self.bst = BSTNode()
        self.users = get_users(5)
        for user in self.users:
            self.bst.insert(user)

    def test_insert_and_exists(self):
        new_user = User(100)
        self.assertFalse(self.bst.exists(new_user))
        self.bst.insert(new_user)
        self.assertTrue(self.bst.exists(new_user))

    def test_min_max(self):
        expected_min = min(self.users)
        expected_max = max(self.users)
        self.assertEqual(self.bst.get_min(), expected_min)
        self.assertEqual(self.bst.get_max(), expected_max)

    def test_traversals(self):
        inorder = self.bst.inorder([])
        self.assertEqual(inorder, sorted(self.users))

        preorder = self.bst.preorder([])
        self.assertIsInstance(preorder, list)
        self.assertEqual(set(preorder), set(self.users))

        postorder = self.bst.postorder([])
        self.assertIsInstance(postorder, list)
        self.assertEqual(set(postorder), set(self.users))

    def test_height(self):
        h = self.bst.height()
        self.assertIsInstance(h, int)
        self.assertGreaterEqual(h, 1)


def test_delete_leaf(self):
    leaf = self.users[0]
    self.assertTrue(self.bst.exists(leaf))
    self.bst = self.bst.delete(leaf)
    self.assertFalse(self.bst.exists(leaf))


def test_delete_root(self):
    root_val = self.bst.val
    self.assertTrue(self.bst.exists(root_val))
    self.bst = self.bst.delete(root_val)
    self.assertFalse(self.bst.exists(root_val))


if __name__ == "__main__":
    unittest.main()
