def depth_first_search(graph, start_node):
    """
    Perform a Depth-First Search (DFS) on a graph starting from a specified node.

    Parameters:
        graph (dict): A dictionary where keys are nodes and values are lists of neighboring nodes.
        start_node: The node to start the DFS traversal from.

    Returns:
        set: A set of nodes visited during the DFS traversal.
    """
    def dfs_recursive(graph, current_node, visited):
        visited.add(current_node)  # Mark the current node as visited
        for neighbor in graph.get(current_node, []):  # Safely handle missing keys
            if neighbor not in visited:  # Visit unvisited neighbors
                dfs_recursive(graph, neighbor, visited)
        return visited

    # Initialize visited set and call the recursive function
    visited_nodes = dfs_recursive(graph, start_node, set())
    return visited_nodes


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

    # Perform DFS starting from node 'A'
    visited_nodes = depth_first_search(graph_example, 'A')
    print("Visited nodes in DFS order:", visited_nodes)
