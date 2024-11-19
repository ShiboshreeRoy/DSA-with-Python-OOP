def breadth_first_search(graph, start_node):
    """
    Perform a Breadth-First Search (BFS) on a graph starting from a specified node.

    Parameters:
        graph (dict): A dictionary where keys are nodes and values are lists of neighboring nodes.
        start_node: The node to start the BFS traversal from.

    Returns:
        set: A set of nodes visited during the BFS traversal.
    """
    visited = set()  # Set to keep track of visited nodes
    queue = [start_node]  # Initialize a queue with the start node

    while queue:
        current_node = queue.pop(0)  # Dequeue the first element
        if current_node not in visited:  # Process unvisited nodes
            visited.add(current_node)  # Mark as visited
            for neighbor in graph.get(current_node, []):  # Safely handle missing keys
                if neighbor not in visited:  # Enqueue unvisited neighbors
                    queue.append(neighbor)

    return visited


# Example usage:
if __name__ == "__main__":
    # Graph represented as an adjacency list
    graph_example = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Perform BFS starting from node 'A'
    visited_nodes = breadth_first_search(graph_example, 'A')
    print("Visited nodes in BFS order:", visited_nodes)
