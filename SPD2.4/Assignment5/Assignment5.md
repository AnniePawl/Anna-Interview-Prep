## Given a singly-linked list, find the middle value in the list.
**Example:** If the given linked list is A → B → C → D → E, return C.

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
    def append(self, value)
    node = Node(value)
    if self.head = None: # if LL empty, set head 
      self.head = node
      self.tail = self.head
    else: # if not empty, add to tail, update tail 
      self.tail.next = node
      self.tail = self.tail.next # reset tail

```