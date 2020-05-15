## Given a binary search tree, reverse the order of its values by modifying the nodes’ links.

### Sample Input:
```python
     6
    /   \
   3     4
  / \   / \
 7   3 8   1
```

### Sample Output:
```python
     6
    /   \
   4     3
  / \   / \
 1   8 3   7
```

```python 
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

  # Reverse tree w/ stack ?
  # Time Complexity: O(n)
  def reverse(root):
    stack = [root]
    while stack:
      node = stack.pop(-1)
      if node:
        node.left, node.right = node.right, node.left 
        stack.append(node.left)
        stack.append(node.right)
    return root 

```