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

    def remove_between_nodes(self, existing_data):
        if not self.head or not self.head.next:
            print("Linked list is empty or has only one node. Cannot remove between nodes.")
            return

        current = self.head
        previous = None

        while current.next:
            if current.data == existing_data and current.next:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next

                print(f"Removed node with data {current.data} between nodes.")
                return

            previous = current
            current = current.next

        print(f"No node found with data {existing_data} between nodes.")

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
my_linked_list.append(4)

# Display the linked list
print("Linked List:")
my_linked_list.display()

# Remove the node with data 2 between nodes
my_linked_list.remove_between_nodes(2)

# Display the linked list after removal
print("Linked List after removing between nodes:")
my_linked_list.display()
