# Write a method called remove_duplicates() that removes all duplicate nodes from a sorted linked list

# 3 3 4 4 5 5 5


def remove_duplicates(self):


    # set current head
current_node = self.head

# is the list is not empty?
if current_node is None:
    return
    # loop while there are nodes
    while current_node.next is not None:
        if current_node.data == current_node.next.data:
            new_node = current_node.next.next
            current_node.next = None           current_node.next = new_node else: current_node = current.next
            return self.head

# Jess' Example


def remove_duplicates(self):
    current = self.head
    while current.next != None:
        if current.data == current.next.data  # found duplicate
        current.next = next_next
        else:
            cuurent = current.next
