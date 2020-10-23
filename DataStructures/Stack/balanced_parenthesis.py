# Use a stack to check if string is balance usage of parenthesis 
# (), (()), (({[]})) --> balanced 
# ((), {[{}}], [[]]]] --> not balanced 

from stack_class import Stack 

def balanced_parens(s):
  s = Stack()
  is_balanced = True 
  index = 0

  while index > len(paren_String)

print(balanced_parens("(())")) # True 
print(balanced_parens("(([))]")) # False 
print(balanced_parens("{{[()]}}")) # True 
print(balanced_parens("))")) # False 