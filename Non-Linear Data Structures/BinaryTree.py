class Node:
    """A class representing a single node in a binary tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    """A class representing a binary tree."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the binary tree."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        """Helper method for recursive insertion."""
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)

    def search(self, key):
        """Search for a key in the binary tree."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        """Helper method for recursive search."""
        if current is None:
            return False
        if key == current.key:
            return True
        elif key < current.key:
            return self._search_recursive(current.left, key)
        else:
            return self._search_recursive(current.right, key)

    def delete(self, key):
        """Delete a node with the specified key."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current, key):
        """Helper method for recursive deletion."""
        if current is None:
            return current

        if key < current.key:
            current.left = self._delete_recursive(current.left, key)
        elif key > current.key:
            current.right = self._delete_recursive(current.right, key)
        else:
            # Node with one child or no child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(current.right)
            current.key = temp.key
            current.right = self._delete_recursive(current.right, temp.key)

        return current

    def _min_value_node(self, node):
        """Find the node with the smallest key."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def in_order_traversal(self):
        """Perform in-order traversal."""
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.key)
            self._in_order_recursive(node.right, result)

    def pre_order_traversal(self):
        """Perform pre-order traversal."""
        result = []
        self._pre_order_recursive(self.root, result)
        return result

    def _pre_order_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)

    def post_order_traversal(self):
        """Perform post-order traversal."""
        result = []
        self._post_order_recursive(self.root, result)
        return result

    def _post_order_recursive(self, node, result):
        if node:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.key)

    def level_order_traversal(self):
        """Perform level-order traversal (breadth-first search)."""
        result = []
        if self.root is None:
            return result
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.key)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def height(self):
        """Calculate the height of the tree."""
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

    def is_balanced(self):
        """Check if the binary tree is balanced."""
        def check(node):
            if node is None:
                return 0, True
            left_height, left_balanced = check(node.left)
            right_height, right_balanced = check(node.right)
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            return max(left_height, right_height) + 1, balanced

        _, balanced = check(self.root)
        return balanced

    def count_nodes(self):
        """Count the total number of nodes in the tree."""
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    def find_min(self):
        """Find the minimum key in the tree."""
        if self.root is None:
            return None
        return self._min_value_node(self.root).key

    def find_max(self):
        """Find the maximum key in the tree."""
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key

bt = BinaryTree()

# Insert nodes
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(2)
bt.insert(7)

# Traversals
print("In-order Traversal:", bt.in_order_traversal())
print("Pre-order Traversal:", bt.pre_order_traversal())
print("Post-order Traversal:", bt.post_order_traversal())
print("Level-order Traversal:", bt.level_order_traversal())

# Search and Delete
print("Search 7:", bt.search(7))
bt.delete(7)
print("Search 7 after deletion:", bt.search(7))

# Height and Balancing
print("Height of tree:", bt.height())
print("Is tree balanced?:", bt.is_balanced())

# Count Nodes, Min, Max
print("Number of nodes:", bt.count_nodes())
print("Minimum value:", bt.find_min())
print("Maximum value:", bt.find_max())
