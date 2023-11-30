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

    def remove_from_end(self):
        if not self.head:
            print("Linked list is empty. Cannot remove from the end.")
            return

        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            print(f"Removed the only node with data {removed_data} from the end.")
            return

        current = self.head
        previous = None

        while current.next:
            previous = current
            current = current.next

        removed_data = current.data
        previous.next = None
        print(f"Removed node with data {removed_data} from the end.")

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

# Remove a node from the end of the linked list
my_linked_list.remove_from_end()

# Display the linked list after removal
print("Linked List after removing from the end:")
my_linked_list.display()
