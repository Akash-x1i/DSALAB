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

    def insert_between_nodes(self, existing_data, new_data):
        new_node = Node(new_data)

        current = self.head
        while current:
            if current.data == existing_data:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
my_linked_list = LinkedList()

# Append elements to the linked list
my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.append(5)

# Display the linked list
print("Linked List:")
my_linked_list.display()

# Insert a new node with data 2 between nodes with data 1 and 3
my_linked_list.insert_between_nodes(1, 2)

# Display the linked list after insertion
print("Linked List after insertion between nodes:")
my_linked_list.display()
