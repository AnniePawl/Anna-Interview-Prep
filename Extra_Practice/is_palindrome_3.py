# Determine if string is palindrome 

def is_palindrome(s):
  # Create two pointers(one traverses forward, one backwards)
  i = 0
  j = len(s)-1
  
  while i < j:
    # Account for non alphabetical chars
    while not s[i].isalpha():
      i +=1 
    while not s[j].isalpha():
      j -=1
  
    if s[i].lower() != s[j].lower():
      return False 

    i +=1 
    j -=1
  return True

print(is_palindrome('Anna')) # True 
print(is_palindrome('Race Car!')) # True 
print(is_palindrome('grouch')) # False