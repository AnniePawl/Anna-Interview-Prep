# Given string of chars, reverse in place using O(1) extra mem

def reverse(chars):
  for i in range(1,len(chars)):
    chars.insert(0,chars.pop(i))
  return chars

print(reverse(["h","e","l","l","o"]))
# ["o","l","l","e","h"]


# Swap 
def reverse2(chars):
  left = 0 
  right = len(chars) - 1 
  # stop when hit middle 
  while left < right:
    # swap outside elements 
    chars[left], chars[right] = chars[right], chars[left]
    # move towards middle 
    left +=1
    right -=1
  return chars

print(reverse2(["c", "a", "t"])) 