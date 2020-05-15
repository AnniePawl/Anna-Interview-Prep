## SPD Assignment 4: Rotate linked list counter-clockwise by k nodes 

```python 
# Node Class 
class Node(self, data):
  def __init__(self, data):
    self.data = data 
    self.next =  None 
     
# LinkedList Class
class LinkedList():
  def __init__(self, items=[]):
    self.head = None 
    self.tail = None
    # append items to LL
    for item  in n items:
      self.append(item)

    # append method
    def append(self, value):
      node = Node(value)
      if self.head = None: 
        self.head = node
        self.tail = self.head
      else: 
        self.tail.next = node
        self.tail = self.tail.next


    # ROTATE BY K NODES

    # Sample LL = 1 -> 2 -> 3 -> 4 -> 5 -> 6
    # K = 3 
    # Sample Output = 4 -> 5-> 6-> 1 ->2 -> 3

    # Patterns: 
      # Kth node always becomes tail
      # Kth + 1 node always becomes head 
      # Original tail always points to original head

    # rotate method 
    def rotate(self, k):
      if k == 0: # base case
        return 
      
      current = self.head # initialize temp node
      count = 0  # index of current node

      # Keep track of old head and tail 
      old_head = self.head 
      old_tail = self.tail 

      # Keep track of new head and tail 
      new_head = 
      new_tail = 

      # loop to find kth node 
      while current.next is not None:
        if count == k:
          new_head = current.data
          new_tail = current.next 
        current = current.next




     

```