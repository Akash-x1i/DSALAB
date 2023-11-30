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

    def insert_between_nodes(self, existing_data, new_data):
        new_node = Node(new_data)

        if not self.head:
            print("Circular Linked List is empty. Cannot insert between nodes.")
            return

        current = self.head

        while True:
            if current.data == existing_data and current.next != self.head:
                new_node.next = current.next
                current.next = new_node
                print(f"Inserted node with data {new_data} between nodes.")
                return
            elif current.data == existing_data and current.next == self.head:
                # Insert at the end, after the last node
                current.next = new_node
                new_node.next = self.head
                print(f"Inserted node with data {new_data} between nodes.")
                return
            current = current.next

            if current == self.head:
                break

        print(f"No node found with data {existing_data}. Cannot insert between nodes.")

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
my_circular_linked_list.append(3)
my_circular_linked_list.append(5)

# Display the circular linked list
print("Circular Linked List:")
my_circular_linked_list.display()

# Insert a new node with data 2 between nodes with data 1 and 3
my_circular_linked_list.insert_between_nodes(1, 2)

# Display the circular linked list after insertion between nodes
print("Circular Linked List after insertion between nodes:")
my_circular_linked_list.display()
