class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_between_nodes(self, existing_data, new_data):
        new_node = Node(new_data)

        if not self.head:
            print("Doubly linked list is empty. Cannot insert between nodes.")
            return

        current = self.head

        while current:
            if current.data == existing_data and current.next:
                new_node.prev = current
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
                print(f"Inserted node with data {new_data} between nodes.")
                return
            current = current.next

        print(f"No node found with data {existing_data}. Cannot insert between nodes.")

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Example usage:
my_doubly_linked_list = DoublyLinkedList()

# Append elements to the doubly linked list
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(5)

# Display the doubly linked list forward
print("Doubly Linked List (Forward):")
my_doubly_linked_list.display_forward()

# Insert a new node with data 2 between nodes with data 1 and 3
my_doubly_linked_list.insert_between_nodes(1, 2)

# Display the doubly linked list forward after insertion between nodes
print("Doubly Linked List (Forward) after insertion between nodes:")
my_doubly_linked_list.display_forward()
