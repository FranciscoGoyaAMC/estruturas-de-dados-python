class Graph:
    """
    Classe Graph representa um grafo não direcionado usando um dicionário de adjacências.

    Métodos:
        adjacent_nodes(node): Retorna os vizinhos de um nó.
        add_edge(u, v): Adiciona uma aresta entre dois nós.
        unconnected_vertices(): Retorna os vértices sem conexões.
        edge_exists(u, v): Verifica se existe uma aresta entre dois nós.
        breadth_first_search(v): Busca em largura a partir de um nó.
        depth_first_search(start_vertex): Busca em profundidade a partir de um nó.
        __repr__(): Retorna uma representação em string do grafo.
    """

    def __init__(self):
        """
        Inicializa o grafo como um dicionário vazio.
        """
        self.graph = {}  # Dicionário de adjacências: nó -> conjunto de vizinhos

    def adjacent_nodes(self, node):
        """
        Retorna os nós adjacentes (vizinhos) de um nó.

        Args:
            node: O nó cujos vizinhos serão retornados.

        Returns:
            set: Conjunto de nós vizinhos.
        """
        return self.graph[node]  # Retorna o conjunto de vizinhos do nó

    def add_edge(self, u, v):
        """
        Adiciona uma aresta não direcionada entre os nós u e v.

        Args:
            u: Um dos nós da aresta.
            v: Outro nó da aresta.
        """
        if u not in self.graph:
            self.graph[u] = set()  # Cria o conjunto de vizinhos se não existir
        if v not in self.graph:
            self.graph[v] = set()
        self.graph[u].add(v)  # Adiciona v como vizinho de u
        self.graph[v].add(u)  # Adiciona u como vizinho de v (grafo não direcionado)

    def unconnected_vertices(self):
        """
        Retorna uma lista de vértices sem conexões (grau zero).

        Returns:
            list: Lista de vértices sem vizinhos.
        """
        return [v for v, neighbors in self.graph.items() if not neighbors]  # Filtra vértices sem vizinhos

    def edge_exists(self, u, v):
        """
        Verifica se existe uma aresta entre os nós u e v.

        Args:
            u: Um dos nós.
            v: Outro nó.

        Returns:
            bool: True se a aresta existe, False caso contrário.
        """
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])  # Verifica se ambos são vizinhos
        return False

    def breadth_first_search(self, v):
        """
        Realiza busca em largura (BFS) a partir do nó v.

        Args:
            v: Nó inicial da busca.

        Returns:
            list: Lista de vértices visitados em ordem de descoberta.
        """
        visited_vertices = []  # Lista de vértices visitados
        vertices_to_explore = [v]  # Fila de vértices a explorar
        while vertices_to_explore:
            current = vertices_to_explore.pop(0)  # Remove o primeiro da fila
            if current not in visited_vertices:
                visited_vertices.append(current)  # Marca como visitado
                neighbors = sorted(self.graph[current])  # Ordena os vizinhos para visita determinística
                for neighbor in neighbors:
                    if neighbor not in visited_vertices and neighbor not in vertices_to_explore:
                        vertices_to_explore.append(neighbor)  # Adiciona vizinhos não visitados à fila
        return visited_vertices

    def depth_first_search(self, start_vertex):
        """
        Realiza busca em profundidade (DFS) a partir do nó start_vertex.

        Args:
            start_vertex: Nó inicial da busca.

        Returns:
            list: Lista de vértices visitados em ordem de descoberta.
        """
        visited_vertices = []  # Lista de vértices visitados
        self.depth_first_search_r(visited_vertices, start_vertex)  # Chama função recursiva auxiliar
        return visited_vertices

    def depth_first_search_r(self, visited, current_vertex):
        """
        Função recursiva auxiliar para busca em profundidade.

        Args:
            visited (list): Lista de vértices visitados.
            current_vertex: Vértice atual.
        """
        visited.append(current_vertex)  # Marca o vértice atual como visitado
        sorted_neighbors = sorted(self.graph[current_vertex])  # Ordena vizinhos para visita determinística
        for neighbor in sorted_neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)  # Chama recursivamente para vizinhos não visitados

    def __repr__(self):
        """
        Retorna uma representação em string do grafo, mostrando vértices e suas conexões.

        Returns:
            str: Representação do grafo.
        """
        result = ""  # String acumuladora
        for key in self.graph.keys():  # Para cada vértice
            result += f"Vertex: '{key}'\n"  # Mostra o vértice
            for v in sorted(self.graph[key]):  # Para cada vizinho ordenado
                result += f"has an edge leading to --> {v} \n"  # Mostra a conexão
        return result  # Retorna a string final
