class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point back to the head, creating the circular link
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head  # Point back to the head

    def append_node(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point back to the head, creating the circular link
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head  # Point back to the head

    def display(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(" (Back to Head)")

# Example usage:
my_circular_linked_list = CircularLinkedList()

# Append elements to the circular linked list
my_circular_linked_list.append(1)
my_circular_linked_list.append(2)
my_circular_linked_list.append(3)

# Display the circular linked list
print("Circular Linked List:")
my_circular_linked_list.display()

# Append a new node to the circular linked list
my_circular_linked_list.append_node(4)

# Display the circular linked list after appending a node
print("Circular Linked List after appending a node:")
my_circular_linked_list.display()
