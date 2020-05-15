# Write a function that will reverse a integer number using a stack and return the reversed number as an integer. For example, if your input number is 3479 the function will return 9743. 

# Strategy: Push digits from number into stack. Pop contents one-by-one to form reversed number 

class Stack():
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []
   
  def push(self, item):
    self.items.append(item)
  
  def pop(self):
    return self.items.pop()

def reverse_num(stack, number):
  # Turn number into string to access each value individually
  num_array = [int(num) for num in number]
  print(num_array)
  
  for num in num_array:
    stack.push(num)

    reversed_num_array = []
    reversed_num_array = stack.pop(num)

  return reversed_num_array

  
stack = Stack()
print(reverse_num(stack, 12345))


