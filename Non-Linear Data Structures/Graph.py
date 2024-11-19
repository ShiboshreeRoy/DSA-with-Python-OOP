class Graph:
    def __init__(self):
        """Initialize an empty graph."""
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, is_directed=False):
        """Add an edge between two vertices."""
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            if not is_directed:
                self.adjacency_list[vertex2].append(vertex1)
        else:
            raise ValueError("One or both vertices not found in graph.")

    def remove_vertex(self, vertex):
        """Remove a vertex and its edges."""
        if vertex in self.adjacency_list:
            # Remove the vertex from adjacency list of other vertices
            for adjacent in self.adjacency_list[vertex]:
                self.adjacency_list[adjacent].remove(vertex)
            # Remove the vertex itself
            del self.adjacency_list[vertex]

    def remove_edge(self, vertex1, vertex2):
        """Remove an edge between two vertices."""
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

    def bfs(self, start_vertex):
        """Perform Breadth-First Search (BFS) and return the visited nodes."""
        visited = set()
        queue = [start_vertex]
        bfs_result = []

        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                bfs_result.append(current)
                queue.extend(self.adjacency_list[current])

        return bfs_result

    def dfs(self, start_vertex):
        """Perform Depth-First Search (DFS) and return the visited nodes."""
        visited = set()
        stack = [start_vertex]
        dfs_result = []

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                dfs_result.append(current)
                stack.extend(self.adjacency_list[current])

        return dfs_result

    def display(self):
        """Display the graph's adjacency list."""
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex} -> {', '.join(edges)}")


g = Graph()

# Add vertices
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

# Add edges
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

# Display the graph
g.display()

# Perform BFS and DFS
print("BFS:", g.bfs("A"))
print("DFS:", g.dfs("A"))

# Remove an edge and display the graph again
g.remove_edge("A", "B")
g.display()

# Remove a vertex and display the graph
g.remove_vertex("D")
g.display()
