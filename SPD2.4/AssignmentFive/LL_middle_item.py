# Given a singly-linked list, find the middle value in the list.
# Example: If the given linked list is A → B → C → D → E, return C.
# Assumptions: The length (n) is odd so the linked list has a definite middle.

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

def findMiddle(L):
  # array itialized to store index to value 
  items_array = []
  curr = L.head
  # append values to array 
  while curr != None: # loop until pointer = none
    items_array.append(curr.data)
    curr = curr.next 
  middle = len(items_array)//2   # find middle index 
  return items_array[middle] # return middle value


# Test! 
def testFindMiddleValue():
  L = LinkedList(["a", "b", "c"])
  print("Passed!")
  assert(findMiddle(L) == "b")
  
testFindMiddleValue()




