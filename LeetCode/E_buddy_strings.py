#  Given strings A and B (all lowercase), return True if you can swap 2 letters in A to get B. Otherwise return False

# Different Lengths --> F 
# Same String

def buddy_string(a,b):

  
  

print(buddy_string('ab', 'ba')) # True
print(buddy_string('ab', 'ab')) # False
print(buddy_string('aa', 'aa')) # True
print(buddy_string('aab', 'aa')) # False
print(buddy_string('abc', 'acb')) # True