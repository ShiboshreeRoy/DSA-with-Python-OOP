class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the end
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            print("Node not found.")
            return
        prev.next = current.next
        current = None

    # Search for a node by value
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Display all nodes in the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Get the length of the linked list
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

# Usage example
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.display()  # Output: 10 -> 20 -> 30 -> None
print("Length:", linked_list.length())  # Output: Length: 3

linked_list.delete(20)
linked_list.display()  # Output: 10 -> 30 -> None

print("Is 30 in the list?", linked_list.search(30))  # Output: True
print("Is 20 in the list?", linked_list.search(20))  # Output: False
