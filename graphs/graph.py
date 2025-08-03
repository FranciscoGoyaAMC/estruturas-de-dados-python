class Graph:
    def __init__(self):
        self.graph = {}

    def adjacent_nodes(self, node):
        return self.graph[node]

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set()
        if v not in self.graph:
            self.graph[v] = set()
        self.graph[u].add(v)
        self.graph[v].add(u)

    def unconnected_vertices(self):
        return [v for v, neighbors in self.graph.items() if not neighbors]

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False

    def breadth_first_search(self, v):
        visited_vertices = []
        vertices_to_explore = [v]
        while vertices_to_explore:
            current = vertices_to_explore.pop(0)
            if current not in visited_vertices:
                visited_vertices.append(current)
                neighbors = sorted(self.graph[current])
                for neighbor in neighbors:
                    if neighbor not in visited_vertices and neighbor not in vertices_to_explore:
                        vertices_to_explore.append(neighbor)
        return visited_vertices

    def depth_first_search(self, start_vertex):
        visited_vertices = []
        self.depth_first_search_r(visited_vertices, start_vertex)
        return visited_vertices

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        sorted_neighbors = sorted(self.graph[current_vertex])
        for neighbor in sorted_neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
