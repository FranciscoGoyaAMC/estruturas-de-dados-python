from rb_tree import RBTree
from user import get_users


def in_order(node, nil, result):
    if node != nil:
        in_order(node.left, nil, result)
        result.append(node.val)
        in_order(node.right, nil, result)


def test_rb_tree_insert():
    tree = RBTree()
    users = get_users(10)

    for user in users:
        tree.insert(user)

    # Test 1: raiz deve ser preta
    assert tree.root.red is False, "A raiz deve ser preta."

    # Test 2: a árvore deve conter os usuários ordenados por ID (in-order traversal)
    result = []
    in_order(tree.root, tree.nil, result)
    sorted_users = sorted(users)
    assert result == sorted_users, "A travessia in-order não corresponde à ordenação esperada."

    # Test 3: propriedade da árvore rubro-negra - não há dois vermelhos consecutivos
    def no_double_red(node):
        if node == tree.nil:
            return True
        if node.red:
            if node.left.red or node.right.red:
                return False
        return no_double_red(node.left) and no_double_red(node.right)

    assert no_double_red(tree.root), "Não deve haver dois nós vermelhos consecutivos."

    print("Todos os testes passaram!")


if __name__ == "__main__":
    test_rb_tree_insert()
