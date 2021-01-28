# Given a string, return True if it's a palindrome 
# Palindrome --> word/ phrase read same backward and forwards
# Example --> "racecar"
# Example --> "Race Car!!" caps, whitespace, punctuation

import string 

# Strategy One 
def palindrome(s):
  s = s.replace(" ","")# remove whitespaces 
  s = s.lower()# Make letters lowercase
  # remove punctuation
  s = s.translate(str.maketrans('','',string.punctuation))
  # check is word is same backwards
  return s == s[::-1]

print(palindrome("racecar")) # True
print(palindrome("Race Car!!")) # True
print(palindrome("peanut")) # False


# Strategy Two 
def is_palindrome2(s):
# Create two pointers to traverse string 
  i = 0
  j = len(s)-1
  # Keep going until reach middle OR until two letters don't match 
  while i < j:
  # Check if char is a whitespace of punctuation 
    while not s[i].isalpha():
      i+=1
    while not s[j].isalpha():
      j -=1
  # Check if letters are same 
    if s[i].lower() != s[j].lower():
      return False
  # Otherwise, increment/ decrement pointers
    i +=1
    j-=1

  return True


print(is_palindrome2("racecar")) # True
print(is_palindrome2("Race Car!!")) # True
print(is_palindrome2("peanut")) # False