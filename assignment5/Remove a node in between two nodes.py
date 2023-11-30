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

    def remove_between_nodes(self, existing_data):
        if not self.head:
            print("Circular Linked List is empty. Cannot remove between nodes.")
            return

        current = self.head
        prev = None

        while True:
            if current.data == existing_data and current.next != self.head:
                if prev:
                    prev.next = current.next
                else:
                    # Removing the first node
                    while current.next != self.head:
                        current = current.next
                    current.next = self.head.next
                    self.head = self.head.next

                print(f"Removed node with data {existing_data} between nodes.")
                return
            prev = current
            current = current.next

            if current == self.head:
                break

        print(f"No node found with data {existing_data} between nodes.")

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
my_circular_linked_list.append(4)

# Display the circular linked list
print("Circular Linked List:")
my_circular_linked_list.display()

# Remove the node with data 2 between nodes
my_circular_linked_list.remove_between_nodes(2)

# Display the circular linked list after removal between nodes
print("Circular Linked List after removal between nodes:")
my_circular_linked_list.display()
