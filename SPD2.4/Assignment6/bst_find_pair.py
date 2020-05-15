# Binary Tree Nodes:
class Node:
  def __init__(self, data):
    self.data = data 
    self.left = None 
    self.right = None

# Binary Tree 
class BinaryTree:
  def __init__(self):
    self.root = None # No nodes yet
  
  def insert(self,item):
    if self.root == None:
      # create new instance of node class w/ item
      self.root = node(item) 
    else:
      self._insert(item, self.root)