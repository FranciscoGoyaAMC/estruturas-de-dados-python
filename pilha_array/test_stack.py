from stack import Stack

def test_stack_operations():
    pilha = Stack()

    assert pilha.size() == 0
    assert pilha.peek() is None
    assert pilha.pop() is None

    pilha.push("A")
    pilha.push("B")
    pilha.push("C")

    assert pilha.size() == 3
    assert pilha.peek() == "C"

    assert pilha.pop() == "C"
    assert pilha.pop() == "B"
    assert pilha.pop() == "A"

    assert pilha.pop() is None
    assert pilha.size() == 0

    print("Todos os testes de pilha passaram!")

if __name__ == "__main__":
    test_stack_operations()
