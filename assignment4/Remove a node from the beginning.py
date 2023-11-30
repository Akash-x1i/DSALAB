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

    def remove_from_beginning(self):
        if not self.head:
            print("Doubly linked list is empty. Cannot remove from the beginning.")
            return

        removed_data = self.head.data
        if self.head.next:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            # Only one node in the list
            self.head = None
            self.tail = None

        print(f"Removed node with data {removed_data} from the beginning.")

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

# Display the doubly linked list forward
print("Doubly Linked List (Forward):")
my_doubly_linked_list.display_forward()

# Remove a node from the beginning of the doubly linked list
my_doubly_linked_list.remove_from_beginning()

# Display the doubly linked list forward after removal
print("Doubly Linked List (Forward) after removal from the beginning:")
my_doubly_linked_list.display_forward()
