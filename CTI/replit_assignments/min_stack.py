# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # Create LL
        self.head= None
        self.smallest = None 
        return 

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.head:
          # create new node 
          new_node = LinkedNode(x)
          if x < self.smallest.data:
            self.smallest = new_node
          new_node.next 
        

    def pop(self):
        """
        :rtype: None
        """
        if sel.head:
          new_head = self.head.next
          element = self.head 
          

    def top(self):
        """
        :rtype: int
        """
        return
        

    def getMin(self):
        """
        :rtype: int
        """
        return
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()