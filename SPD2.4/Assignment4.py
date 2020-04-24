"""
PROBLEM: Rotate a given linked list counter-clockwise by k nodes, where k is a given integer.

Q: What clarifying questions would you ask?
- Are LL classes already defined?
- Is this doublely or single LL?

Q: What reasonable assumptions could you state?


Q: What are 2-3 ways you can simplify the problem?
- LL has 2 nodes , k = 1

Brainstorm 2-3 ways to approach the problem.
"""


class Node:
    # Constructor
    def__init__(self, data=None, next=None):
    self.data = data
    self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
