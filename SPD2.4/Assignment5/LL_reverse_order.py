# Given a singly linked list, reverse order by modifying node's links 

# Node Class 
class Node():
  def __init__(self, data):
    self.data = data 
    self.next =  None 
     
# LinkedList Class
class LinkedList():
  def __init__(self, items=[]):
    self.head = None 
    self.tail = None
    # append items to LL
    for item in items:
      self.append(item)

  # append method
  def append(self, value):
    node = Node(value)
    if self.head is None: # if LL empty, set head 
      self.head = node
      self.tail = self.head
    else: # if not empty, add to tail, update tail 
      self.tail.next = node
      self.tail = self.tail.next # reset tail

  def reverse_order(L):
    prev = None
    current = self.head 
    while current is not None:
      next = current.next 
      current.next = prev 
      prev = current 
      current = next
    self.head = prev
      
  
# Test! 
def testReverseOrder():
  L = LinkedList(["a", "b", "c"])
  print("Passed!")
  assert(reverse_order(L) == ["c", "b", "a"])
  
testReverseOrder()