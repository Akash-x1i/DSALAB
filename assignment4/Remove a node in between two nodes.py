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

    def remove_between_nodes(self, existing_data):
        if not self.head or not self.head.next:
            print("Doubly linked list is empty or has only one node. Cannot remove between nodes.")
            return

        current = self.head

        while current.next:
            if current.data == existing_data and current.next:
                if current.prev:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    # Removing the first node
                    current.next.prev = None
                    self.head = current.next

                print(f"Removed node with data {existing_data} between nodes.")
                return
            current = current.next

        print(f"No node found with data {existing_data} between nodes.")

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
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)

# Display the doubly linked list forward
print("Doubly Linked List (Forward):")
my_doubly_linked_list.display_forward()

# Remove the node with data 2 between nodes
my_doubly_linked_list.remove_between_nodes(2)

# Display the doubly linked list forward after removal between nodes
print("Doubly Linked List (Forward) after removal between nodes:")
my_doubly_linked_list.display_forward()
