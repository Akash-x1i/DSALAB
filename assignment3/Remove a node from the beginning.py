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

    def remove_from_beginning(self):
        if not self.head:
            print("Linked list is empty. Cannot remove from the beginning.")
            return

        removed_data = self.head.data
        self.head = self.head.next

        print(f"Removed node with data {removed_data} from the beginning.")

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
my_linked_list.append(2)
my_linked_list.append(3)

# Display the linked list
print("Linked List:")
my_linked_list.display()

# Remove a node from the beginning of the linked list
my_linked_list.remove_from_beginning()

# Display the linked list after removal
print("Linked List after removing from the beginning:")
my_linked_list.display()
