# Given a string, considering only alphanumeric chars and ignoring cases, check if string is palindrome 

import string 

def is_palindrome(s):
  pass 

print(is_palindrome("race car")) # True
print(is_palindrome("gross")) # False
print(is_palindrome("A man, a plan, a canal: Panama")) # True







# Method One (shortcut) 
def palindrome(s):
  s = s.lower() # make lowercase
  s = s.replace(" ","") # remove whitepace 
  # Remove punctuation
  s = s.translate(str.maketrans('','',string.punctuation))
  return s == s[::-1]

print(palindrome("race car")) # True
print(palindrome("gross")) # False
print(palindrome("A man, a plan, a canal: Panama")) # True

