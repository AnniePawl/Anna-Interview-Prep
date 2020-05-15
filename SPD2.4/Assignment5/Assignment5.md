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


    def findMiddle(L):  #O(n)
      # Time O(n)
      # Space O(n)
      # array itialized to store index to value 
      items_array = [] # O(1)
      curr = L.head # O(1)
      # append values to array 
      while curr != None: # loop until pointer = none # O(n)
        items_array.append(curr.data) # O(n)
        curr = curr.next  #O(1)
      middle = len(items_array)//2   # find middle index O(1)
      return items_array[middle] # return middle value O(1)

    # Test! 
    def testFindMiddleValue():
      L = LinkedList(["a", "b", "c"])
      print("Passed!")
      assert(findMiddle(L) == "b")
  
    testFindMiddleValue()

```

## Given a singly linked list, reverse order by modifying node's links 

```python 
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
  
```