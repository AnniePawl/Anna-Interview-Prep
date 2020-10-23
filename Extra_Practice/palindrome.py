# Given a string, considering only alphanumeric chars and ignoring cases, check if string is palindrome 

import string 

# Better Solution b/c only requires linear time, and not linear space
def is_palindrome(s):
  # Iterator i will move from front to back 
  #  Iterator j will move from back to from 
  i = 0  # start of string 
  j = len(s) -1 # start at back of string

  while i < j:
    while not s[i].isalnum() and i <j:
      i += 1 # move i over one 
    while not s[j].isalnum() and i <j:
      j -= 1
    if s[i].lower() !=s[j].lower():
      return False

    i +=1  # increment i 
    j -=1 # decrement j

  return True

print("Method One")  
print(is_palindrome("race car")) # True
print(is_palindrome("gross")) # False
print(is_palindrome("A man, a plan, a canal: Panama")) # True






# Method Two (shortcut) 
# This solution takes up extra space proportional to size of string. Linear time and linear space 0(n)
def palindrome(s):
  # Normalize the case  by removing extra chars and space, etc
  s = s.lower() # make lowercase
  s = s.replace(" ","") # remove whitepace 
  # Remove punctuation
  s = s.translate(str.maketrans('','',string.punctuation))
  # 
  return s == s[::-1] # 0(n)


print("Method Two")
print(palindrome("race car")) # True
print(palindrome("gross")) # False
print(palindrome("A man, a plan, a canal: Panama")) # True

