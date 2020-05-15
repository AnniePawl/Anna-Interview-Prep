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
```