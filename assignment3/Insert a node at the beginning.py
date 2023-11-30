class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data, next=self.head)
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
my_linked_list = LinkedList()

# Append elements to the linked list
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

# Display the linked list
print("Linked List:")
my_linked_list.display()

# Insert a new node at the beginning of the linked list
my_linked_list.insert_at_beginning(1)

# Display the linked list after inserting at the beginning
print("Linked List after inserting at the beginning:")
my_linked_list.display()
