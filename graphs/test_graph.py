from graph import Graph


def test_add_edge_and_adjacency():
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')

    assert g.adjacent_nodes('A') == {'B', 'C'}
    assert g.adjacent_nodes('B') == {'A', 'D'}
    assert g.adjacent_nodes('C') == {'A'}
    assert g.adjacent_nodes('D') == {'B'}


def test_edge_exists():
    g = Graph()
    g.add_edge('X', 'Y')
    assert g.edge_exists('X', 'Y') is True
    assert g.edge_exists('Y', 'X') is True
    assert g.edge_exists('X', 'Z') is False


def test_unconnected_vertices():
    g = Graph()
    g.graph = {
        'A': set(),
        'B': {'C'},
        'C': {'B'},
        'D': set()
    }
    assert set(g.unconnected_vertices()) == {'A', 'D'}


def test_breadth_first_search():
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('E', 'F')

    result = g.breadth_first_search('A')
    assert result == ['A', 'B', 'C', 'D', 'E', 'F']


def test_depth_first_search():
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('E', 'F')

    result = g.depth_first_search('A')
    assert result == ['A', 'B', 'D', 'C', 'E', 'F']


def test_repr():
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')

    output = repr(g)
    assert "Vertex: 'A'" in output
    assert "has an edge leading to --> B" in output
    assert "has an edge leading to --> C" in output


if __name__ == "__main__":
    test_add_edge_and_adjacency()
    test_edge_exists()
    test_unconnected_vertices()
    test_breadth_first_search()
    test_depth_first_search()
    test_repr()
    print("Todos os testes passaram com sucesso! ✅")
