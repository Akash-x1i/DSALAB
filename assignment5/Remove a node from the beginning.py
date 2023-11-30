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

    def remove_from_beginning(self):
        if not self.head:
            print("Circular Linked List is empty. Cannot remove from the beginning.")
            return

        removed_data = self.head.data
        if self.head.next != self.head:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        else:
            # Only one node in the list
            self.head = None

        print(f"Removed node with data {removed_data} from the beginning.")

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

# Remove a node from the beginning of the circular linked list
my_circular_linked_list.remove_from_beginning()

# Display the circular linked list after removal from the beginning
print("Circular Linked List after removal from the beginning:")
my_circular_linked_list.display()
