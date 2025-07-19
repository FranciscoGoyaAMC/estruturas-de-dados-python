from node import Node
from llqueue import LLQueue


def test_llqueue_operations():
    fila = LLQueue()

    assert fila.remove_from_head() is None

    fila.add_to_tail(Node("A"))
    fila.add_to_tail(Node("B"))
    fila.add_to_tail(Node("C"))

    # Verificando a ordem de remoção (FIFO)
    assert fila.remove_from_head().val == "A"
    assert fila.remove_from_head().val == "B"

    fila.add_to_tail(Node("D"))
    assert fila.remove_from_head().val == "C"
    assert fila.remove_from_head().val == "D"
    assert fila.remove_from_head() is None

    print("Todos os testes de fila passaram!")


if __name__ == "__main__":
    test_llqueue_operations()
    